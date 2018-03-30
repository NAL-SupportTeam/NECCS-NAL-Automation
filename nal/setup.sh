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
LOG_DIR=log/construct/$DATETIME
mkdir -p $LOG_DIR

echo "${DATETIME} : Start [${NODE_TYPE}]" > ${LOG_DIR}/setup.log

if [ $NODE_TYPE == "all" -o  $NODE_TYPE == "lb" ]; then
  DATETIME=`date '+%Y%m%d%H%M%S'`
  echo "${DATETIME} : Exec ansible-playbook -i ${HOST_LIST} ${PLAYBOOK_DIR}/01_nallb.yml" >> ${LOG_DIR}/setup.log
  ansible-playbook -i ${HOST_LIST} ${PLAYBOOK_DIR}/01_nallb.yml 2>&1 | tee ${LOG_DIR}/nallb.log
fi
if [ $NODE_TYPE == "all" -o  $NODE_TYPE == "web" ]; then
  DATETIME=`date '+%Y%m%d%H%M%S'`
  echo "${DATETIME} : Exec ansible-playbook -i ${HOST_LIST} ${PLAYBOOK_DIR}/02_nalweb.yml" >> ${LOG_DIR}/setup.log
  ansible-playbook -i ${HOST_LIST} ${PLAYBOOK_DIR}/02_nalweb.yml 2>&1 | tee ${LOG_DIR}/nalweb.log
fi
if [ $NODE_TYPE == "all" -o  $NODE_TYPE == "ap" ]; then
  DATETIME=`date '+%Y%m%d%H%M%S'`
  echo "${DATETIME} : Exec ansible-playbook -i ${HOST_LIST} ${PLAYBOOK_DIR}/03_nalap.yml" >> ${LOG_DIR}/setup.log
  ansible-playbook -i ${HOST_LIST} ${PLAYBOOK_DIR}/03_nalap.yml 2>&1 | tee ${LOG_DIR}/nalap.log
fi
if [ $NODE_TYPE == "all" -o  $NODE_TYPE == "db" ]; then
  DATETIME=`date '+%Y%m%d%H%M%S'`
  echo "${DATETIME} : Exec ansible-playbook -i ${HOST_LIST} ${PLAYBOOK_DIR}/04_naldb.yml" >> ${LOG_DIR}/setup.log
  ansible-playbook -i ${HOST_LIST} ${PLAYBOOK_DIR}/04_naldb.yml 2>&1 | tee ${LOG_DIR}/naldb.log
fi
if [ $NODE_TYPE == "all" -o  $NODE_TYPE == "fe" ]; then
  DATETIME=`date '+%Y%m%d%H%M%S'`
  echo "${DATETIME} : Exec ansible-playbook -u root -i ${HOST_LIST} ${PLAYBOOK_DIR}/05_nalfe.yml" >> ${LOG_DIR}/setup.log
  ansible-playbook -u root -i ${HOST_LIST} ${PLAYBOOK_DIR}/05_nalfe.yml 2>&1 | tee ${LOG_DIR}/nalfe.log
fi

DATETIME=`date '+%Y%m%d%H%M%S'`
echo "${DATETIME} : End" >> ${LOG_DIR}/setup.log
