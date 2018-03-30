#!/usr/bin/sh

CMDNAME=`basename $0`

usage() {
  echo "Usage: $CMDNAME [<ndoe-type>]" 1>&2
  echo "  <ndoe-type>: node type" 1>&2
  echo "    lb  : Web Loadbaranser" 1>&2
  echo "    web : Web Server" 1>&2
  echo "    ap  : AP Server" 1>&2
  echo "    db  : DB Server" 1>&2
  echo "    fe  : Frotend Server" 1>&2
  echo "" 1>&2
}

if [ $# -gt 1 ]; then
  echo -e "error: too many parameter.\n" 1>&2
  usage
  exit 1
fi

NODES=("lb" "web" "ap" "db" "fe")
NODE_TYPE=""

if [ $# -eq 0 ]; then
  NODE_TYPE="all"
else
  for type in "${NODES[@]}"
  do
    if [ $1 == $type ]; then
      NODE_TYPE=$1
      break
    fi
  done
fi

if [ "$NODE_TYPE" = "" ]; then
  echo -e "error: invalid parameter.\n" 1>&2
  usage
  exit 1
fi

HOST_LIST=hosts.ini
PLAYBOOK_DIR=playbooks

DATETIME=`date '+%Y%m%d%H%M%S'`
LOG_DIR=log/ut/$DATETIME
mkdir -p $LOG_DIR

echo "${DATETIME} : Start [${NODE_TYPE}]" > ${LOG_DIR}/unittest.log

if [ $NODE_TYPE == "all" -o  $NODE_TYPE == "lb" ]; then
  DATETIME=`date '+%Y%m%d%H%M%S'`
  echo "${DATETIME} : Exec ansible-playbook -i ${HOST_LIST} ${PLAYBOOK_DIR}/31_naltest_ut_lb.yml 2>&1 | tee ${LOG_DIR}/nallb.log" >> ${LOG_DIR}/unittest.log
  ansible-playbook -i ${HOST_LIST} ${PLAYBOOK_DIR}/31_naltest_ut_lb.yml 2>&1 | tee ${LOG_DIR}/nallb.log
fi
if [ $NODE_TYPE == "all" -o  $NODE_TYPE == "web" ]; then
  DATETIME=`date '+%Y%m%d%H%M%S'`
  echo "${DATETIME} : Exec ansible-playbook -i ${HOST_LIST} ${PLAYBOOK_DIR}/32_naltest_ut_web.yml 2>&1 | tee ${LOG_DIR}/nalweb.log" >> ${LOG_DIR}/unittest.log
  ansible-playbook -i ${HOST_LIST} ${PLAYBOOK_DIR}/32_naltest_ut_web.yml 2>&1 | tee ${LOG_DIR}/nalweb.log
fi
if [ $NODE_TYPE == "all" -o  $NODE_TYPE == "ap" ]; then
  DATETIME=`date '+%Y%m%d%H%M%S'`
  echo "${DATETIME} : Exec ansible-playbook -i ${HOST_LIST} ${PLAYBOOK_DIR}/33_naltest_ut_ap.yml 2>&1 | tee ${LOG_DIR}/nalap.log" >> ${LOG_DIR}/unittest.log
  ansible-playbook -i ${HOST_LIST} ${PLAYBOOK_DIR}/33_naltest_ut_ap.yml 2>&1 | tee ${LOG_DIR}/nalap.log
fi
if [ $NODE_TYPE == "all" -o  $NODE_TYPE == "db" ]; then
  DATETIME=`date '+%Y%m%d%H%M%S'`
  echo "${DATETIME} : Exec ansible-playbook -i ${HOST_LIST} ${PLAYBOOK_DIR}/34_naltest_ut_db.yml 2>&1 | tee ${LOG_DIR}/naldb.log" >> ${LOG_DIR}/unittest.log
  ansible-playbook -i ${HOST_LIST} ${PLAYBOOK_DIR}/34_naltest_ut_db.yml 2>&1 | tee ${LOG_DIR}/naldb.log
fi
if [ $NODE_TYPE == "all" -o  $NODE_TYPE == "fe" ]; then
  DATETIME=`date '+%Y%m%d%H%M%S'`
  echo "${DATETIME} : Exec ansible-playbook -u root -i ${HOST_LIST} ${PLAYBOOK_DIR}/30_naltest_ut_fe.yml 2>&1 | tee ${LOG_DIR}/nalfe.log" >> ${LOG_DIR}/unittest.log
  ansible-playbook -u root -i ${HOST_LIST} ${PLAYBOOK_DIR}/30_naltest_ut_fe.yml 2>&1 | tee ${LOG_DIR}/nalfe.log
fi

DATETIME=`date '+%Y%m%d%H%M%S'`
echo "${DATETIME} : End" >> ${LOG_DIR}/unittest.log
