package nbtool.gui;

import java.awt.Dimension;
import java.awt.event.ComponentAdapter;
import java.awt.event.ComponentEvent;

import javax.swing.JList;
import javax.swing.JPanel;
import javax.swing.JScrollPane;
import javax.swing.JTree;
import javax.swing.ListSelectionModel;
import javax.swing.tree.TreePath;
import javax.swing.tree.TreeSelectionModel;

import nbtool.data.Log;

public class LogChooser extends JPanel {
	private static final long serialVersionUID = 1L;
	public LogChooser() {
		setLayout(null);
		addComponentListener(new ComponentAdapter() {
			public void componentResized(ComponentEvent e) {
				useSize(e.getComponent().getSize());
			}
		});
				
		model = new LCTreeModel();
		tree = new JTree(model);
		model.tree = tree;
		tree.setEditable(false);
		tree.setRootVisible(false);
		tree.setScrollsOnExpand(true);
		tree.getSelectionModel().setSelectionMode(TreeSelectionModel.DISCONTIGUOUS_TREE_SELECTION);
		tree.addTreeSelectionListener(model);
		tree.setTransferHandler(model.EXPORT_HANDLER);
		tree.setDragEnabled(true);
		
		sas = new SortAndSearch(model);
		model.sas = sas;
		
		sp = new JScrollPane(tree);
		sp.setViewportView(tree);
		
		sp.setVerticalScrollBarPolicy(JScrollPane.VERTICAL_SCROLLBAR_ALWAYS);
		sp.setHorizontalScrollBarPolicy(JScrollPane.HORIZONTAL_SCROLLBAR_ALWAYS);
		//sp.setVerticalScrollBarPolicy();
		
		add(sas);
		add(sp);
	}
	
	private void useSize(Dimension size) {
		Dimension d = sas.getPreferredSize();
		sas.setBounds(0,0,d.width,d.height);
		sp.setBounds(0, d.height, size.width, size.height - d.height);
	}
	
	private JScrollPane sp;
	private JTree tree;
	private LCTreeModel model;
	
	private SortAndSearch sas;
}
