#!/bin/bash
LOCKDIR=/tmp/call_hubspot_api-lock
THISRUN=`date +%Y%m%d-%H%M`
LOGFILE=/var/www/vhosts/mcarena/tool_hubspot_mirgation/log/call_hubspot_api.log
FULLPATH=`readlink -f $0`
DIRNAME=`dirname $FULLPATH`
BNAME=`basename $FULLPATH`

. $DIRNAME/common.inc
LOGGER=$DIRNAME/logger.pl

main() {
        do_lock
        python3 /var/www/vhosts/mcarena/tool_hubspot_mirgation/processor.py
        rm -rf "${LOCKDIR}"
}

main 2>&1 | $LOGGER >> $LOGFILE
