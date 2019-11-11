#!/bin/bash
PATH=/usr/local/sbin:/usr/local/bin:/sbin:/bin:/usr/sbin:/usr/bin:/root/bin
export PATH
 

###
### locking: define $LOCKDIR before calling this function
###
do_lock()
{
    LOCK_FD=1000
    local fd=${1:-$LOCK_FD}
    local lock_file=$LOCKDIR/.lock
    #create lockdir
    mkdir -p "${LOCKDIR}" &>/dev/null; 
    #global write access to support apache and root
    touch $lock_file && chmod 777 $lock_file 2>/dev/null 2>&1

    # create lock file
    eval "exec $fd>$lock_file" 

    # acquire the lock
    flock -n $fd && return 0 || { echo "[locking]: lock failed, already locked"; exit 1; }
}