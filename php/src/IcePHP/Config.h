// **********************************************************************
//
// Copyright (c) 2003-2009 ZeroC, Inc. All rights reserved.
//
// This copy of Ice is licensed to you under the terms described in the
// ICE_LICENSE file included in this distribution.
//
// **********************************************************************

#ifndef ICE_PHP_CONFIG_H
#define ICE_PHP_CONFIG_H

//
// We need to define WIN32_LEAN_AND_MEAN to avoid redefinition errors in
// winsock2.h. However, we can't define the macro in the Makefile because
// a PHP header defines it without a surrounding #ifndef, so we have to
// undefine it before including the PHP header files.
//
#ifdef _WIN32
#   define WIN32_LEAN_AND_MEAN
#endif

#include <Ice/Ice.h>
#include <Slice/Parser.h>

#ifdef _WIN32
#   undef WIN32_LEAN_AND_MEAN
#endif

#ifdef _WIN32
#include <crtdbg.h>
#include <math.h>
#endif

#ifdef _WIN32
extern "C"
{
#endif

#include "php.h"
#include "php_ini.h"
#include "ext/standard/info.h"
#include "zend_interfaces.h"
#include "zend_exceptions.h"

#ifdef _WIN32
}
#endif

extern zend_module_entry ice_module_entry;
#define phpext_ice_ptr &ice_module_entry

#ifdef PHP_WIN32
#define PHP_ICE_API __declspec(dllexport)
#else
#define PHP_ICE_API
#endif

#ifdef ZTS
#include "TSRM.h"
#endif

ZEND_MINIT_FUNCTION(ice);
ZEND_MSHUTDOWN_FUNCTION(ice);
ZEND_RINIT_FUNCTION(ice);
ZEND_RSHUTDOWN_FUNCTION(ice);
ZEND_MINFO_FUNCTION(ice);

ZEND_BEGIN_MODULE_GLOBALS(ice)
    zval* communicator;
    void* marshalerMap;
    void* profile;
    void* properties;
    void* objectFactoryMap;
ZEND_END_MODULE_GLOBALS(ice)

#ifdef ZTS
#define ICE_G(v) TSRMG(ice_globals_id, zend_ice_globals*, v)
#else
#define ICE_G(v) (ice_globals.v)
#endif

#endif
