#!/usr/bin/env python
# **********************************************************************
#
# Copyright (c) 2001
# Mutable Realms, Inc.
# Huntsville, AL, USA
#
# All Rights Reserved
#
# **********************************************************************

import sys, os, TestUtil

icePackPort = "0";

def startIcePack(toplevel, port, testdir):

    global icePackPort

    options = TestUtil.clientServerOptions.replace("TOPLEVELDIR", toplevel)

    icePackPort = port
    
    icePack = os.path.join(toplevel, "bin", "icepack")

    print "starting icepack...",
    command = icePack + options + ' --nowarn ' + \
          r' --IcePack.Locator.Endpoints="default -p ' + icePackPort + '  -t 5000" ' + \
          r' --IcePack.LocatorRegistry.Endpoints=default' + \
          r' --IcePack.Admin.Endpoints=default' + \
          r' --IcePack.Yellow.Query=Yellow/Query@YellowQueryAdapter' + \
          r' --IcePack.Yellow.Admin=Yellow/Admin@YellowAdminAdapter' + \
          r' --IcePack.Data=' + os.path.join(testdir, "db") + \
          r' --Ice.ProgramName=icepack' + \
          r' --IcePack.Trace.Activator=0 --IcePack.Trace.AdapterManager=0 --IcePack.Trace.ServerManager=0'

    icePackPipe = os.popen(command)
    TestUtil.getServerPid(icePackPipe)
    TestUtil.getServerPid(icePackPipe)
    TestUtil.getAdapterReady(icePackPipe)
    TestUtil.getAdapterReady(icePackPipe)
    TestUtil.getAdapterReady(icePackPipe)
    TestUtil.getAdapterReady(icePackPipe)
    print "ok"
    return icePackPipe

def shutdownIcePack(toplevel, icePackPipe):

    global icePackPort
    icePackAdmin = os.path.join(toplevel, "bin", "icepackadmin")

    options = TestUtil.clientOptions.replace("TOPLEVELDIR", toplevel)

    print "shutting down icepack...",
    command = icePackAdmin + options + \
              r' "--Ice.Default.Locator=IcePack/Locator:default -p ' + icePackPort + '" ' + \
              r' -e "shutdown" '    

    icePackAdminPipe = os.popen(command)
    icePackAdminStatus = icePackAdminPipe.close()
    icePackPipe.close()
    print "ok"

    if icePackAdminStatus:
        TestUtil.killServers()
        sys.exit(1)
        
def addApplication(toplevel, descriptor, targets):

    global icePackPort
    icePackAdmin = os.path.join(toplevel, "bin", "icepackadmin")

    options = TestUtil.clientOptions.replace("TOPLEVELDIR", toplevel)
    
    command = icePackAdmin + options + \
              r' "--Ice.Default.Locator=IcePack/Locator:default -p ' + icePackPort + '" ' + \
              r' -e "application add \"' + descriptor + '\\" ' + targets + ' \"'

    icePackAdminPipe = os.popen(command)
    icePackAdminStatus = icePackAdminPipe.close()
    if icePackAdminStatus:
        TestUtil.killServers()
        sys.exit(1)

def removeApplication(toplevel, descriptor):

    global icePackPort
    icePackAdmin = os.path.join(toplevel, "bin", "icepackadmin")

    options = TestUtil.clientOptions.replace("TOPLEVELDIR", toplevel)
    
    command = icePackAdmin + options + \
              r' "--Ice.Default.Locator=IcePack/Locator:default -p ' + icePackPort + '" ' + \
              r' -e "application remove \"' + descriptor + '\\" \"'

    icePackAdminPipe = os.popen(command)
    icePackAdminStatus = icePackAdminPipe.close()
    if icePackAdminStatus:
        TestUtil.killServers()
        sys.exit(1)

def addServer(toplevel, name, serverDescriptor, server, libpath, targets):

    global icePackPort
    icePackAdmin = os.path.join(toplevel, "bin", "icepackadmin")

    options = TestUtil.clientOptions.replace("TOPLEVELDIR", toplevel)
    
    command = icePackAdmin + options + \
              r' "--Ice.Default.Locator=IcePack/Locator:default -p ' + icePackPort + '" ' + \
              r' -e "server add \"' + name + '\\" \\"' + serverDescriptor + '\\" ' + \
              r' \"' + server + '\\" \\"' + libpath + '\\" ' + targets + '\"'

    icePackAdminPipe = os.popen(command)
    icePackAdminStatus = icePackAdminPipe.close()
    if icePackAdminStatus:
        TestUtil.killServers()
        sys.exit(1)

def removeServer(toplevel, name):

    global icePackPort
    icePackAdmin = os.path.join(toplevel, "bin", "icepackadmin")

    options = TestUtil.clientOptions.replace("TOPLEVELDIR", toplevel)
    
    command = icePackAdmin + options + \
              r' "--Ice.Default.Locator=IcePack/Locator:default -p ' + icePackPort + '" ' + \
              r' -e "server remove \"' + name + '\\" \"'

    icePackAdminPipe = os.popen(command)
    icePackAdminStatus = icePackAdminPipe.close()
    if icePackAdminStatus:
        TestUtil.killServers()
        sys.exit(1)

def startServer(toplevel, name):
    global icePackPort
    icePackAdmin = os.path.join(toplevel, "bin", "icepackadmin")

    options = TestUtil.clientOptions.replace("TOPLEVELDIR", toplevel)

    command = icePackAdmin + options + \
              r' "--Ice.Default.Locator=IcePack/Locator:default -p ' + icePackPort + '" ' + \
              r' -e "server start \"' + name + '\\""'

    icePackAdminPipe = os.popen(command)
    icePackAdminStatus = icePackAdminPipe.close()
    if icePackAdminStatus:
        TestUtil.killServers()
        sys.exit(1)

def listAdapters(toplevel):
    global icePackPort
    icePackAdmin = os.path.join(toplevel, "bin", "icepackadmin")

    options = TestUtil.clientOptions.replace("TOPLEVELDIR", toplevel)

    command = icePackAdmin + options + \
              r' "--Ice.Default.Locator=IcePack/Locator:default -p ' + icePackPort + '" ' + \
              r' -e "adapter list"'

    icePackAdminPipe = os.popen(command)
    return icePackAdminPipe

def removeAdapter(toplevel, name):

    global icePackPort
    icePackAdmin = os.path.join(toplevel, "bin", "icepackadmin")

    options = TestUtil.clientOptions.replace("TOPLEVELDIR", toplevel)

    command = icePackAdmin + options + \
              r' "--Ice.Default.Locator=IcePack/Locator:default -p ' + icePackPort + '" ' + \
              r' -e "adapter remove \"' + name + '\\""'

    icePackAdminPipe = os.popen(command)
    icePackAdminStatus = icePackAdminPipe.close()
    if icePackAdminStatus:
        TestUtil.killServers()
        sys.exit(1)

