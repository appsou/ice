// **********************************************************************
//
// Copyright (c) 2003
// ZeroC, Inc.
// Billerica, MA, USA
//
// All Rights Reserved.
//
// Ice is free software; you can redistribute it and/or modify it under
// the terms of the GNU General Public License version 2 as published by
// the Free Software Foundation.
//
// **********************************************************************

package Ice;

public class _ObjectDelM implements _ObjectDel
{
    public boolean
    ice_isA(String __id, java.util.Map __context)
        throws IceInternal.NonRepeatable
    {
        IceInternal.Outgoing __out = getOutgoing("ice_isA", OperationMode.Nonmutating, __context);
        try
        {
            IceInternal.BasicStream __is = __out.is();
            IceInternal.BasicStream __os = __out.os();
            __os.writeString(__id);
            if(!__out.invoke())
            {
                throw new UnknownUserException();
            }
            try
            {
                return __is.readBool();
            }
            catch(LocalException __ex)
            {
                throw new IceInternal.NonRepeatable(__ex);
            }
        }
        finally
        {
            reclaimOutgoing(__out);
        }
    }

    public void
    ice_ping(java.util.Map __context)
        throws IceInternal.NonRepeatable
    {
        IceInternal.Outgoing __out = getOutgoing("ice_ping", OperationMode.Nonmutating, __context);
        try
        {
            if(!__out.invoke())
            {
                throw new UnknownUserException();
            }
        }
        finally
        {
            reclaimOutgoing(__out);
        }
    }

    public String[]
    ice_ids(java.util.Map __context)
        throws IceInternal.NonRepeatable
    {
        IceInternal.Outgoing __out = getOutgoing("ice_ids", OperationMode.Nonmutating, __context);
        try
        {
            IceInternal.BasicStream __is = __out.is();
            if(!__out.invoke())
            {
                throw new UnknownUserException();
            }
            try
            {
                return __is.readStringSeq();
            }
            catch(LocalException __ex)
            {
                throw new IceInternal.NonRepeatable(__ex);
            }
        }
        finally
        {
            reclaimOutgoing(__out);
        }
    }

    public String
    ice_id(java.util.Map __context)
        throws IceInternal.NonRepeatable
    {
        IceInternal.Outgoing __out = getOutgoing("ice_id", OperationMode.Nonmutating, __context);
        try
        {
            IceInternal.BasicStream __is = __out.is();
            if(!__out.invoke())
            {
                throw new UnknownUserException();
            }
            try
            {
                return __is.readString();
            }
            catch(LocalException __ex)
            {
                throw new IceInternal.NonRepeatable(__ex);
            }
        }
        finally
        {
            reclaimOutgoing(__out);
        }
    }

    public String[]
    ice_facets(java.util.Map __context)
        throws IceInternal.NonRepeatable
    {
        IceInternal.Outgoing __out = getOutgoing("ice_facets", OperationMode.Nonmutating, __context);
        try
        {
            IceInternal.BasicStream __is = __out.is();
            if(!__out.invoke())
            {
                throw new UnknownUserException();
            }
            try
            {
                return __is.readStringSeq();
            }
            catch(LocalException __ex)
            {
                throw new IceInternal.NonRepeatable(__ex);
            }
        }
        finally
        {
            reclaimOutgoing(__out);
        }
    }

    public boolean
    ice_invoke(String operation, OperationMode mode, byte[] inParams, ByteSeqHolder outParams, java.util.Map __context)
        throws IceInternal.NonRepeatable
    {
        IceInternal.Outgoing __out = getOutgoing(operation, mode, __context);
        try
        {
            IceInternal.BasicStream __os = __out.os();
            __os.writeBlob(inParams);
            boolean ok = __out.invoke();
            if(__reference.mode == IceInternal.Reference.ModeTwoway)
            {
                try
                {
                    IceInternal.BasicStream __is = __out.is();
                    int sz = __is.getReadEncapsSize();
                    outParams.value = __is.readBlob(sz);
                }
                catch(LocalException __ex)
                {
                    throw new IceInternal.NonRepeatable(__ex);
                }
            }
            return ok;
        }
        finally
        {
            reclaimOutgoing(__out);
        }
    }

    //
    // Only for use by ObjectPrx
    //
    final void
    __copyFrom(_ObjectDelM from)
    {
        //
        // No need to synchronize "from", as the delegate is immutable
        // after creation.
        //

        //
        // No need to synchronize, as this operation is only called
        // upon initialization.
        //

	assert(__reference == null);
	assert(__connection == null);

        __reference = from.__reference;
        __connection = from.__connection;
    }

    protected IceInternal.Reference __reference;
    protected IceInternal.Connection __connection;

    public void
    setup(IceInternal.Reference ref)
    {
        //
        // No need to synchronize, as this operation is only called
        // upon initialization.
        //

	assert(__reference == null);
	assert(__connection == null);

	__reference = ref;
	__connection = __reference.getConnection();
    }
    
    protected IceInternal.Outgoing
    getOutgoing(String operation, OperationMode mode, java.util.Map context)
    {
        IceInternal.Outgoing out;

        synchronized(__outgoingMutex)
        {
            if(__outgoingCache == null)
            {
                out = new IceInternal.Outgoing(__connection, __reference, operation, mode, context);
            }
            else
            {
                out = __outgoingCache;
                __outgoingCache = __outgoingCache.next;
                out.reset(operation, mode, context);
            }
        }

        return out;
    }

    protected void
    reclaimOutgoing(IceInternal.Outgoing out)
    {
	//
	// TODO: Is this code necessary? Shouldn't __outgoingCache be
	// empty, i.e., shouldn't this be assert(__outgoingCache ==
	// null), just like for _incomingCache in
	// IceInternal::Connection?
	//
        synchronized(__outgoingMutex)
        {
            out.next = __outgoingCache;
            __outgoingCache = out;
        }
    }

    protected void
    finalize()
        throws Throwable
    {
        while(__outgoingCache != null)
        {
            IceInternal.Outgoing next = __outgoingCache.next;
            __outgoingCache.destroy();
            __outgoingCache.next = null;
            __outgoingCache = next;
        }
    }

    private IceInternal.Outgoing __outgoingCache;
    private java.lang.Object __outgoingMutex = new java.lang.Object();
}
