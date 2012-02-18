/**
 * @class OverseerServer
 *
 * Simple server class that listens for an inbound connection,
 * and then starts a threaded logger that streams current ground truth data to the client
 *
 * @author Octavian Neamtu
 *
 */


#pragma once

#include <vector>

#include "Structs.h"
#include "io/MessageInterface.h"
#include "synchro/synchro.h"

namespace nbites {
namespace overseer {

class OverseerServer : public Thread {

public:
    static const unsigned short OVERSEER_PORT = 42424;

public:

    OverseerServer(point<float>* ballPosition,
                   std::vector<point<float> >* robotPositions);
    virtual ~OverseerServer();

    virtual void run();

    virtual void postData();

private:
    common::io::MessageInterface::ptr groundTruthMessage;

};

}
}