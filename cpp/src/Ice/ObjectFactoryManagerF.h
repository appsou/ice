// **********************************************************************
//
// Copyright (c) 2003-2009 ZeroC, Inc. All rights reserved.
//
// This copy of Ice is licensed to you under the terms described in the
// ICE_LICENSE file included in this distribution.
//
// **********************************************************************

#ifndef ICE_SERVANT_FACTORY_MANAGER_F_H
#define ICE_SERVANT_FACTORY_MANAGER_F_H

#include <IceUtil/Shared.h>

#include <Ice/Handle.h>

namespace IceInternal
{

class ObjectFactoryManager;
IceUtil::Shared* upCast(ObjectFactoryManager*);
typedef Handle<ObjectFactoryManager> ObjectFactoryManagerPtr;

}

#endif
