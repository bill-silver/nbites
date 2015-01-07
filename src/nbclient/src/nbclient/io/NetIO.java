package nbclient.io;


import java.io.BufferedInputStream;
import java.io.BufferedOutputStream;
import java.io.DataInputStream;
import java.io.DataOutputStream;
import java.io.IOException;
import java.io.InputStream;
import java.io.OutputStream;
import java.net.Socket;
import java.net.UnknownHostException;

import nbclient.data.Log;
import nbclient.data.Log.SOURCE;
import nbclient.util.P;
import nbclient.util.U;

/**
 * NetIO objects are connections to a single robot.  They are intended to constitute the run loop of their own thread.
 * 
 * When the connection is closed or the NetIO object believes the connection has been lost, 
 * they return run() ending the thread.
 * 
 * When a full object has been retrieved from the network it is delivered to <boss>.
 * 
 * the 'Boss' object is expected to determine what type of Object it is being given...
 * 
 * NOTE:  <takeDelivery> is called in the NetIO run-loop.  Therefore the implementation of takeDelivery should NOT do
 * any extensive calculations; it should in some way mark that data has arrived, save the data, and wait for a separate
 * thread to pick up on the new data.
 * */

public class NetIO implements Runnable {
	public String server_address;
	public int server_port;
	
	public interface Boss {
		void takeDelivery(Log log);
		void netThreadExiting();
	}
	public Boss boss;
	
	public volatile boolean running;
	public InputStream _is;
	public OutputStream _os;
	
	public void run() {
		Socket socket = null;
		try {
			U.w("NetIO: thread created with sa=" + server_address + " sp=" + server_port);
			assert(server_address != null && server_port != 0 && boss != null);
			socket = new Socket(this.server_address, this.server_port);
			BufferedOutputStream _out =  new BufferedOutputStream(socket.getOutputStream());
			BufferedInputStream _in = new BufferedInputStream(socket.getInputStream());
			
			DataOutputStream out = new DataOutputStream(_out);
			DataInputStream in = new DataInputStream(_in);
			_os = out;
			_is = in;
			
			U.w("NetIO: thread connected.");
			//initiate connection
			
			out.writeInt(0);
			out.flush();
			
			int recv = in.readInt();
			if (recv != 0)
				throw new SequenceErrorException(0, recv);
			
			out.writeInt(P.VERSION);
			out.flush();
			recv = in.readInt();
			if (recv != P.VERSION) {
				U.w("WARNING: NetIO connected to robot with version " + recv + 
						" but client is running version " + P.VERSION + " !!\n");
			}
			
			int seq_num = 1;
			while(true) {
				checkRunning();
				
				recv = in.readInt();
				
				if (recv == 0) {
					out.writeInt(0);
					out.flush();
				} else if (recv == seq_num) {
					Log nl = CommonIO.readLog(in);
					U.w("NetIO: thread got packet of data size: " + nl.bytes.length + " desc: " + nl.description);
					
					nl.source = SOURCE.NETWORK;
					
					boss.takeDelivery(nl);
					++seq_num;
				} else {
					throw new SequenceErrorException(seq_num, recv);
				}
			}
		}
		
		catch (UnknownHostException uke) {
			uke.printStackTrace();
			U.w("NetIO thread:" + uke.getMessage());
		}
		catch (IOException ie) {
			ie.printStackTrace();
			U.w("NetIO thread:" + ie.getMessage());
		}
		catch(OutOfMemoryError e) {
			e.printStackTrace();
			U.w("NetIO thread got OutOfMemoryError.");
		}
		catch(NegativeArraySizeException nase) {
			nase.printStackTrace();
			U.w("NetIO got negative incoming data size!");
		}
		catch(SequenceErrorException see) {
			U.w("NetIO thread got out of sequence, exiting!" +
					"\n\texpected:" + see.expected + " was:" + see.was);
		}
		catch (NetClosedException e) {
			U.w("NetIO thread finishing because !running.");
			if (socket != null)
				try {
					socket.close();
				} catch (IOException e1) {
					e1.printStackTrace();
				}
			
			boss.netThreadExiting();
			return;
		}
		
		U.w("NetIO thread exiting atypically...");
		if (socket != null) {
			try {
				socket.close();
			} catch (IOException e) {
				// TODO Auto-generated catch block
				e.printStackTrace();
			}
		}
		
		boss.netThreadExiting();
	}
	
	private static class SequenceErrorException extends Exception {
		public int expected, was;
		SequenceErrorException(int e, int w) {
			super();
			expected = e; was = w;
		}
	}
	
	private static class NetClosedException extends Exception {}
	
	private void checkRunning() throws NetClosedException {
		if (!running) {
			throw new NetClosedException();
		}
	}
	
	public void readExactly(InputStream in, byte[] array) throws IOException, NetClosedException {
		int read = 0;
		while (read < array.length) {
			checkRunning();
			read += in.read(array, read, array.length - read);
		}
	}
}