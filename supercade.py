#!/usr/bin/python
#
# very rudimentary supercade command line client
# (c) 2014 Pau Oliva Fora
#
# [MC-NMF]: .NET Message Framing Protocol Specification
# http://download.microsoft.com/download/9/5/E/95EF66AF-9026-4BB0-A41D-A4F81802D92C/[MC-NMF].pdf
#
# [MC-NBFX]: .NET Binary Format: XML Data Structure
# http://download.microsoft.com/download/9/5/E/95EF66AF-9026-4BB0-A41D-A4F81802D92C/[MC-NBFX].pdf
#
# [MC-NBFSE] .NET Binary Format: SOAP Extension
# http://download.microsoft.com/download/9/5/E/95EF66AF-9026-4BB0-A41D-A4F81802D92C/[MC-NBFSE].pdf
#
# maybe useful:
#  https://github.com/bluec0re/python-wcfbin
#  http://blogs.msdn.com/b/drnick/archive/2009/02/06/message-framing-part-7.aspx
#  http://const.me/articles/net-tcp/ 
#  https://github.com/waf/WCF-Binary-Message-Inspector

import socket
import string
import re
import time

EMAIL=""
PASSWORD=""

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('damdai.com', 7000))

# Initiator Receiver: Preamble Message
#   Version: 1.0
#   Mode: Duplex
#   Binary Session Encoding
s.send('\x00\x01\x00\x01\x02\x02' + '\x20' + "net.tcp://damdai.com:7000/Server" + '\x03\x08')

# Initiator Receiver: Preamble End Message 
s.send('\x0c') # preamble end record

# 0xb == Preamble Ack Message
data = s.recv(4096)
print "(PreambleAckMessage) HEX: ",repr(data)

print "[] Login"
#record_type = '\x06' # Sized Envelope Record (1 byte)
#size = '' # variable (See section 2.2.2 Record Size Encoding of MC-NMF)
#payload_record_type = '\x03' # known_encoding record (1 byte)
#payload_encoding =
#payload = payload_record_type + payload_encoding
#pdu = record_type + size + payload




#  Each byte of the size adds 7 bits to the size field and uses the most significant bit to indicate whether the size has more bytes. When the most significant bit is 1, the next byte in the stream continues the size. When the most significant bit is 0, the size is done
# size here is '81 02'.  (80 + 02>>7) - See section 2.2.2 Record Size Encoding of MC-NMF.
s.send(
#'\x06\xf1\x01\x80\x01'
'\x06\x81\x02\x80\x01'

 + '\x20' + "http://tempuri.org/IServer/Login" + '\x20' + "net.tcp://damdai.com:7000/Server" + '\x05' + "Login" + '\x13' + "http://tempuri.org/" + '\x0c' + "emailAddress" + '\x08' + "password" + '\x0d' + "clientVersion" + '\x56\x02\x0b\x01\x73\x04\x0b\x01\x61\x06\x56\x08\x44\x0a\x1e\x00\x82\xab\x01\x44\x1a\xad' + 

#'\xf4\x83\x84\x4b\xab\xad\x3a\x4d\xbb\x0f\x0f\x78\x47\xdb\x05\x95'
'\x1c\x3f\x33\x1e\xb7\x4c\x51\x4d\xb3\xb2\x75\xa3\x91\xdb\x46\x7a'

 + '\x44\x2c\x44\x2a\xab\x14\x01\x44\x0c\x1e\x00\x82\xab\x03\x01\x56\x0e\x42\x05\x0a\x07\x42\x09\x99' + chr(len(EMAIL)) + EMAIL + '\x42\x0b\x99' + chr(len(PASSWORD)) + PASSWORD + '\x42\x0d\x99' + '\x0e' + "3.0.4528.20515" + '\x01\x01\x01')
data = s.recv(4096)
print "(LoginResult) HEX: ",repr(data)

#testfile = open("prova.bin", "wb")
#testfile.write(data)
#testfile.close()

print "[] RegisterGames"
#pdu='\x06\xfc\x01\xaa\x01\x28' + "http://tempuri.org/IServer/RegisterGames" + '\x0d' + "RegisterGames" + '\x08' + "playerId" + '\x05' + "games" + '\x39' + "http://schemas.microsoft.com/2003/10/Serialization/Arrays" + '\x29' + "http://www.w3.org/2001/XMLSchema-instance" + '\x56\x02\x0b\x01\x73\x04\x0b\x01\x61\x06\x56\x08\x44\x0a\x1e\x00\x82\xab\x0f\x44\x1a\xad\xb0\xc0\x43\x7d\x9b\xc4\xca\x44\xb1\x49\x66\x3c\xfd\x56\x4c\xa5\x44\x2c\x44\x2a\xab\x14\x01\x44\x0c\x1e\x00\x82\xab\x03\x01\x56\x0e\x42\x11\x0a\x07\x42\x13\x8d\x65\xc1\x02\x00\x42\x15\x0b\x01\x62\x17\x0b\x01\x69\x19\x01\x01\x01\x01'
pdu='\x06\x8d\x02\xae\x01\x28' + "http://tempuri.org/IServer/RegisterGames" + '\x0d' + "RegisterGames" + '\x08' + "playerId" + '\x05' + "games" + '\x39' + "http://schemas.microsoft.com/2003/10/Serialization/Arrays" + '\x29' + "http://www.w3.org/2001/XMLSchema-instance" + '\x03\x69\x6e\x74\x56\x02\x0b\x01\x73\x04\x0b\x01\x61\x06\x56\x08\x44\x0a\x1e\x00\x82\xab\x0f\x44\x1a\xad\xb8\xd1\xaf\xe6\xdd\x7c\x30\x43\xb7\x53\x6f\x64\x3f\x49\x7d\x8f\x44\x2c\x44\x2a\xab\x14\x01\x44\x0c\x1e\x00\x82\xab\x03\x01\x56\x0e\x42\x11\x0a\x07\x42\x13\x8d\x66\xc1\x02\x00\x42\x15\x0b\x01\x62\x17\x0b\x01\x69\x19\x45\x1b\x89\x4b\x45\x1b\x89\x4c\x45\x1b\x8b\xd5\x00\x01\x01\x01\x01'



s.send(pdu)
#testfile = open("prova.bin", "wb")
#testfile.write(pdu)
#testfile.close()


data = s.recv(4096)
print "(PlayerHasGames) HEX: ",repr(data)
time.sleep(5)

data = s.recv(4096)
print "(RegisterGamesResponse) HEX: ",repr(data)


print "[] GetPlayers"
#s.send('\x06\x70\x31\x25' + "http://tempuri.org/IServer/GetPlayers" + '\x0a' + "GetPlayers" + '\x56\x02\x0b\x01\x73\x04\x0b\x01\x61\x06\x56\x08\x44\x0a\x1e\x00\x82\xab\x1b\x44\x1a\xad\xbb\xb2\x58\xab\x3b\x06\xdd\x41\xb4\x6f\x5d\xd3\xe9\xe2\x3c\x7b\x44\x2c\x44\x2a\xab\x14\x01\x44\x0c\x1e\x00\x82\xab\x03\x01\x56\x0e\x42\x1d\x0a\x07\x01\x01\x01')
s.send('\x06\x70\x31\x25' + "http://tempuri.org/IServer/GetPlayers" + '\x0a' + "GetPlayers" + '\x56\x02\x0b\x01\x73\x04\x0b\x01\x61\x06\x56\x08\x44\x0a\x1e\x00\x82\xab\x1d\x44\x1a\xad\x35\xda\xd5\xdd\x54\xd4\xcc\x45\xa9\xb7\x9a\x43\x07\xc3\xc5\x4e\x44\x2c\x44\x2a\xab\x14\x01\x44\x0c\x1e\x00\x82\xab\x03\x01\x56\x0e\x42\x1f\x0a\x07\x01\x01\x01')

data = s.recv(4096)
print "(GetPlayersResponse) HEX: ",repr(data)

print "[] GetBlockedPlayers"
#s.send('\x06\x85\x01\x3f\x2c' + "http://tempuri.org/IServer/GetBlockedPlayers" + '\x11' + "GetBlockedPlayers" + '\x56\x02\x0b\x01\x73\x04\x0b\x01\x61\x06\x56\x08\x44\x0a\x1e\x00\x82\xab\x1f\x44\x1a\xad\xea\x5c\xd8\x02\x26\x2e\x29\x4c\xab\x33\x52\x04\xe8\x1d\x12\xa0\x44\x2c\x44\x2a\xab\x14\x01\x44\x0c\x1e\x00\x82\xab\x03\x01\x56\x0e\x42\x21\x0a\x07\x42\x13\x8d\x65\xc1\x02\x00\x01\x01\x01')
s.send('\x06\x85\x01\x3f\x2c' + "http://tempuri.org/IServer/GetBlockedPlayers" + '\x11' + "GetBlockedPlayers" + '\x56\x02\x0b\x01\x73\x04\x0b\x01\x61\x06\x56\x08\x44\x0a\x1e\x00\x82\xab\x21\x44\x1a\xad\x6d\x07\x08\x19\xf0\x03\xdd\x4b\x9e\xc2\x18\xc7\x21\x48\x4a\x58\x44\x2c\x44\x2a\xab\x14\x01\x44\x0c\x1e\x00\x82\xab\x03\x01\x56\x0e\x42\x23\x0a\x07\x42\x13\x8d\x66\xc1\x02\x00\x01\x01\x01')


data = s.recv(4096)
print "(GetBlockedPlayersResponse) HEX: ",repr(data)

print "[] JoinRoom"
#s.send('\x06\x7e\x34\x23' + "http://tempuri.org/IServer/JoinRoom" + '\x08' + "JoinRoom" + '\x06' + "roomId" + '\x56\x02\x0b\x01\x73\x04\x0b\x01\x61\x06\x56\x08\x44\x0a\x1e\x00\x82\xab\x23\x44\x1a\xad\x39\xc3\x7e\xed\x33\xb5\x49\x4e\x81\x33\x55\xe9\x82\x0e\x87\xc9\x44\x2c\x44\x2a\xab\x14\x01\x44\x0c\x1e\x00\x82\xab\x03\x01\x56\x0e\x42\x25\x0a\x07\x42\x13\x8d\x65\xc1\x02\x00\x42\x27\x89\x43\x01\x01\x01')
s.send('\x06\x7e\x34\x23' + "http://tempuri.org/IServer/JoinRoom" + '\x08' + "JoinRoom" + '\x06' + "roomId" + '\x56\x02\x0b\x01\x73\x04\x0b\x01\x61\x06\x56\x08\x44\x0a\x1e\x00\x82\xab\x25\x44\x1a\xad\xd0\x8a\x01\xb8\x3f\x29\xa2\x4a\xba\x52\x30\x6c\x15\xd4\x2b\x3c\x44\x2c\x44\x2a\xab\x14\x01\x44\x0c\x1e\x00\x82\xab\x03\x01\x56\x0e\x42\x27\x0a\x07\x42\x13\x8d\x66\xc1\x02\x00\x42\x29\x89\x43\x01\x01\x01')
data = s.recv(4096)
print "(JoinRoomResponse + PlayerJoinedRoom) HEX: ",repr(data)

print "[] TestPort"
#s.send('\x06\x7d\x32\x23' + "http://tempuri.org/IServer/TestPort" + '\x08' + "TestPort" + '\x56\x02\x0b\x01\x73\x04\x0b\x01\x61\x06\x56\x08\x44\x0a\x1e\x00\x82\xab\x29\x44\x1a\xad\xf5\x65\xc7\x2d\x95\x93\xfe\x4b\x9f\x1b\x38\x95\xa6\xda\x11\x50\x44\x2c\x44\x2a\xab\x14\x01\x44\x0c\x1e\x00\x82\xab\x03\x01\x56\x0e\x42\x2b\x0a\x07\x42\x13\x8d\x65\xc1\x02\x00\x42\x2d\x8b\x70\x17\x01\x01\x01')
s.send('\x06\x7d\x32\x23' + "http://tempuri.org/IServer/TestPort" + '\x08' + "TestPort" + '\x56\x02\x0b\x01\x73\x04\x0b\x01\x61\x06\x56\x08\x44\x0a\x1e\x00\x82\xab\x2b\x44\x1a\xad\xb8\xb6\x82\x73\xf0\xca\x72\x46\x88\x97\x0e\xd0\xe3\x1f\x39\xcf\x44\x2c\x44\x2a\xab\x14\x01\x44\x0c\x1e\x00\x82\xab\x03\x01\x56\x0e\x42\x2d\x0a\x07\x42\x13\x8d\x66\xc1\x02\x00\x42\x2f\x8b\x70\x17\x01\x01\x01')
data = s.recv(4096)
print "(TestPortResponse) HEX: ",repr(data)

time.sleep(5)

#s.send('\x06\x81\x01\x33\x22' + "http://tempuri.org/IServer/CanHost" + '\x07' + "CanHost" + '\x07' + "canHost" + '\x56\x02\x0b\x01\x73\x04\x0b\x01\x61\x06\x56\x08\x44\x0a\x1e\x00\x82\xab\x31\x44\x1a\xad\x53\x68\xc9\x8e\x54\xfa\xd1\x41\x81\x89\xdf\x13\xda\x93\xb3\xc6\x44\x2c\x44\x2a\xab\x14\x01\x44\x0c\x1e\x00\x82\xab\x03\x01\x56\x0e\x42\x33\x0a\x07\x42\x13\x8d\x66\xc1\x02\x00\x42\x35\x85\x42\x2f\x8b\x70\x17\x01\x01\x01')
#data = s.recv(4096)
#print "(CanHostResponse) HEX: ",repr(data)


while 1:
	data = s.recv(4096)
	if not data: break

	print "HEX: ",repr(data)

s.close()





#http://tempuri.org/IServer/Login net.tcp://damdai.com:7000/Server
#	http://tempuri.org/IServer/LoginResponse
#
#http://tempuri.org/IServer/RegisterGames
#	http://tempuri.org/IServer/RegisterGamesResponse
#	http://tempuri.org/IServer/PlayerHasGames
#
#http://tempuri.org/IServer/GetPlayers
#	http://tempuri.org/IServer/GetPlayersResponse
#
#http://tempuri.org/IServer/GetBlockedPlayers
#	http://tempuri.org/IServer/GetBlockedPlayersResponse
#
#http://tempuri.org/IServer/JoinRoom
#	http://tempuri.org/IServer/JoinRoomResponse
#	http://tempuri.org/IServer/PlayerJoinedRoom
#
#http://tempuri.org/IServer/TestPort
#	http://tempuri.org/IServer/TestPortResponse
#
#http://tempuri.org/IServer/PlayerCanHost
#
#http://tempuri.org/IServer/CanHost
#	http://tempuri.org/IServer/CanHostResponse
#
#http://tempuri.org/IServer/PlayerStatusChanged
#
#http://tempuri.org/IServer/Challenge
#	http://tempuri.org/IServer/ChallengeResponse
#
#http://tempuri.org/IServer/CancelChallenge
#	http://tempuri.org/IServer/CancelChallengeResponse
#
#http://tempuri.org/IServer/ReceiveRoomChat
#http://tempuri.org/IServer/PlayerOffline
#http://tempuri.org/IServer/PlayerOnline
#
#http://tempuri.org/IServer/ChatPrivate
#	http://tempuri.org/IServer/ChatPrivateResponse
#
#http://tempuri.org/IServer/ChatRoom
#	http://tempuri.org/IServer/ChatRoomResponse
#
#http://tempuri.org/IServer/ChallengeAccepted
#
#     SupercadeEmulator.exe -p2 <p1-ip-address> 6000 "Super Street Fighter II Turbo (super street fighter 2 X 940323 USA)" "<p1-nickname>" "<my-nickname>"
#
#http://tempuri.org/IServer/SetStatus
#	http://tempuri.org/IServer/SetStatusResponse
#
#http://tempuri.org/IServer/ReceiveReplayInfo
#
#http://tempuri.org/IServer/DownloadReplay
#	http://tempuri.org/IServer/DownloadReplayResponse
#
#     SupercadeEmulator.exe -replay "filename.replay" "<p1-nickname>" "<my-nickname>"
#
#http://tempuri.org/IServer/Logout
