
def encryptMessage(key, message):
	j = 0
	cipher = ""
	for i in message:
		cipher += i + key[j]
		j = (j+1) % len(key)
	
	return cipher

def decryptMessage(key, message):
	j = 0
	cipher = ""
	for i in range(0,len(message)):
		if(i % 2):
			j = (j+1) % len(key)
		else:
			cipher+= message[i]
	
	return cipher

myMessage = "TWO roads diverged in a yellow wood,And sorry I could not 
travel both And be one traveler, long I stood And looked down one as far
 as I could To where it bent in the undergrowth Then took the other, as 
just as fair,	And having perhaps the better claim, Because it was grassy
 and wanted wear Though as for that the passing there Had worn them 
really about the same, And both that morning equally lay In leaves no 
step had trodden black. Oh, I kept the first for another day! Yet 
knowing how way leads on to way,	I doubted if I should ever come back. I
 shall be telling this with a sigh Somewhere ages and ages hence	Two 
roads diverged in a wood, and I took the one less traveled by, And that 
has made all the difference."

encrypted = "TMWrOi nraolaMdrsi ndailvMerrigneadl Mirni naa 
lyMerlilnoawl Mwroionda,lAMnrdi nsaolrMrryi nIa lcMoruilnda lnMorti 
ntarlaMvreiln abloMtrhi nAanldM rbien aolnMer itnraalvMerlienra,l 
Mlroinnga lIM rsitnoaoldM rAinnda llMoroikneadl Mdroiwnna loMnrei naasl 
Mfrairn aalsM rIi ncaoluMlrdi nTaol Mwrhienrael Mirti nbaelnMtr iinna 
ltMhrei nuanldMerrignraolwMtrhi nTahleMnr itnoaolkM rtihnea 
loMtrhienra,l Marsi njaulsMtr iansa lfMariirn,a	lAMnrdi nhaalvMirnign 
apleMrrhianpasl Mtrhien ableMtrtienra lcMlraiinma,l MBreicnaaulsMer 
iinta lwMarsi ngarlaMsrsiyn aalnMdr iwnaanltMerdi nwaelaMrr 
iTnhaoluMgrhi naasl Mfroirn atlhMarti ntahleM rpiansasliMnrgi 
ntahleMrrei nHaaldM rwionranl Mtrhienma lrMerailnlayl Marbionuatl 
Mtrhien aslaMmrei,n aAlnMdr ibnoatlhM rtihnaatl MmroirnnailnMgr 
ienqaulaMlrliyn allaMyr iInna llMeraivneasl Mnroi nsatleMpr ihnaadl 
MtrriondadleMnr ibnlaalcMkr.i nOahl,M rIi nkaelpMtr itnhael Mfriirnsatl 
Mfroirn aalnMortihnearl Mdraiyn!a lYMerti nkanloMwriinnga lhMorwi 
nwaalyM rlienaadlsM roinn atloM rwianya,l	MIr idnoaulbMtreidn ailfM rIi 
nsahloMurlidn aelvMerri ncaolmMer ibnaaclkM.r iIn aslhMarliln ableM 
rtienlalliMnrgi ntahliMsr iwniatlhM rai nsailgMhr iSnoamleMwrhienrael 
Margiensa laMnrdi naagleMsr ihneanlcMer	iTnwaol Mrroiandasl 
MdriivnearlgMerdi nianl Mar iwnoaoldM,r iannadl MIr itnoaolkM rtihnea 
loMnrei nlaelsMsr itnraalvMerlienda lbMyr,i nAanldM rtihnaatl Mhraisn 
amlaMdrei naalllM rtihnea ldMirfifnearleMnrcien.a"

myKey = "Rafiscoolmaybe"

encrypt = 1;

if(encrypt == 1):
	print(encryptMessage(myKey,myMessage))
else:
	print(decryptMessage(myKey,encrypted))
	

