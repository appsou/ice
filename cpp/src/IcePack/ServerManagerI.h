// **********************************************************************
//
// Copyright (c) 2001
// Mutable Realms, Inc.
// Huntsville, AL, USA
//
// All Rights Reserved
//
// **********************************************************************

#ifndef ICE_PACK_SERVER_MANAGER_I_H
#define ICE_PACK_SERVER_MANAGER_I_H

#include <IceUtil/Mutex.h>
#include <Freeze/DB.h>
#include <IcePack/ServerManager.h>
#include <IcePack/Activator.h>
#include <set>


namespace IcePack
{

class TraceLevels;
typedef IceUtil::Handle<TraceLevels> TraceLevelsPtr;

class ServerI : public Server, public ::IceUtil::Monitor< ::IceUtil::Mutex>
{
public:

    ServerI(const ::Ice::ObjectAdapterPtr&, const TraceLevelsPtr&, const ActivatorPtr&);
    virtual ~ServerI();
    
    virtual ServerDescription getServerDescription(const ::Ice::Current& = ::Ice::Current());
    virtual bool start(const ::Ice::Current& = ::Ice::Current());
    virtual void stop(const ::Ice::Current& = ::Ice::Current());
    virtual void terminationCallback(const ::Ice::Current& = ::Ice::Current());
    virtual ServerState getState(const ::Ice::Current& = ::Ice::Current());
    virtual Ice::Int getPid(const ::Ice::Current& = ::Ice::Current());

    virtual void setState(ServerState);
    virtual void setPid(int pid);

private:

    ::Ice::ObjectAdapterPtr _adapter;
    TraceLevelsPtr _traceLevels;
    ActivatorPtr _activator;

    ServerState _state;
    int _pid;
};


class ServerManagerI : public ServerManager, public IceUtil::Mutex
{
public:

    ServerManagerI(const Ice::ObjectAdapterPtr&, const TraceLevelsPtr&, const Freeze::DBEnvironmentPtr&,
		   const AdapterManagerPrx&, const ActivatorPtr&);

    virtual ~ServerManagerI();

    virtual ServerPrx create(const ServerDescription&, const ::Ice::Current&);
    virtual ServerPrx findByName(const ::std::string&, const ::Ice::Current&);
    virtual void remove(const ::std::string&, const ::Ice::Current&);
    virtual ServerNames getAll(const ::Ice::Current&);

private:

    ::Ice::ObjectAdapterPtr _adapter;
    TraceLevelsPtr _traceLevels;
    ::Freeze::EvictorPtr _evictor;
    ::std::set< ::std::string> _serverNames;
    AdapterManagerPrx _adapterManager;
    ActivatorPtr _activator;
};

}

#endif
