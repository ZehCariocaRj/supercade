#!/bin/bash
# SupercadeEmulator wrapper script for version v0.2.96.73 (bundled with SuperCade)
# (c)2013-2014 Pau Oliva Fora (@pof)

# This resets pulseaudio on Linux because otherwise FBA hangs on my computer (WTF!?).
# For best results run 'winecfg' and check the option to "Emulate a virtual desktop"
# under the Graphics tab. I've it set to 1152x672 for best full screen aspect ratio.

INSTALLDIR="."

MYDIR=`pwd`
if [ -f "${MYDIR}/SupercadeEmulator.exe" ]; then
	INSTALLDIR=${MYDIR}
fi

FBA="${INSTALLDIR}/SupercadeEmulator.exe"
if [ ! -e ${FBA} ]; then
	echo "-!- cannot find ${INSTALLDIR}/SupercadeEmulator.exe"
	exit 1
fi

function show_usage() {
	echo "USAGE: $0 <ROM> [<P1|P2> <IP>]"
	exit 1
}

ROM=$1

if [ ! -f "${INSTALLDIR}/ROMs/${ROM}.zip" ]; then
	echo "ERROR: Can't find ${INSTALLDIR}/ROMs/${ROM}.zip"
	show_usage
fi

romname=$(strings ${FBA} |grep -A4 "^${ROM}$" |head -n 4 |grep "(" |grep ")$" |head -n 1)
if [ -z "${romname}" ]; then
	echo "ERROR: ROM not supported. Possible roms:"
	strings ${FBA} |grep "^${ROM}" |cut -f -1 -d " " |sort -u |grep -v "^${ROM}$"
	exit 1
fi
echo "-!- rom name: ${romname}"

tot=9999
OS=$(uname -s)
case "${OS}" in
        "Darwin")
		WINE="/Applications/Wine.app/Contents/Resources/bin/wine"
	;;
	"Linux")
		WINE="/usr/bin/wine"

		# check if there are multiple instances running
		tot=$(ps ax |grep SupercadeEmulator.exe |wc -l)

		# first instance resets pulseaudio, others don't
		if [ $tot -eq 0 ]; then
			VOL=$(pacmd dump |grep "^set-sink-volume" |tail -n 1 |awk '{print $3}')
			echo "-!- resetting pulseaudio"
			/usr/bin/pulseaudio -k
			/usr/bin/pulseaudio --start
		fi
	;;
esac

if [ $# -eq 1 ]; then
	${WINE} ${FBA} -1p "${romname}" &
else
	PLAYER=$2
	IP=$3
	if [ -z "${IP}" ]; then show_usage ; fi
	echo "${PLAYER}" |egrep "^[P|p](1|2)$" >/dev/null
	if [ $? -ne 0 ]; then show_usage ; fi
	p=$(echo ${PLAYER} |cut -c 2)
	if [ $p -eq 1 ]; then
		${WINE} ${FBA} -p1 6000 "${romname}" "player1" "player2" "${ROM}_`date "+%Y%m%d-%H%M%S"`.replay" &
	else
		${WINE} ${FBA} -p2 ${IP} 6000 "${romname}" "player1" "player2" &
	fi

fi

if [ $tot -eq 0 ]; then
	sleep 1s
	echo "-!- restoring volume value"
	/usr/bin/pactl set-sink-volume 0 ${VOL}
fi

