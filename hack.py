text = 'AOL MPYZA ZALW PU IYLHRPUN HUF JPWOLY PZ AV AYF AV MPUK MLHABYLZ DOPJO JVYYLZWVUK AV AOL VYPNPUHS WSHPU ALEA DOLYLHZ JVKLZ ZBIZAPABAL NYVBWZ VM SLAALYZ VY MPNBYLZ MVY DVYKZ WOYHZLZ VY LCLU JVTWSLAL JVUJLWAZ JPWOLYZ YLWSHJL LCLYF PUKPCPKBHS SLAALY VM LCLYF DVYK AOLF AOLYLMVYL ALUK AV YLMSLJA AOL JOHYHJALYPZAPJZ VM AOL SHUNBHNL VM AOL VYPNPUHS ALEA AOPZ THRLZ AOLT CBSULYHISL AV ZABKPLZ VM SLAALY MYLXBLUJF MVY LEHTWSL AOL TVZA JVTTVU SLAALYZ PU LUNSPZO HYL L A H V HUK U PM H YLHZVUHISL HTVBUA VY KLWAO VM LUNSPZO ALEA LUJPWOLYLK PU AOL ZHTL ZPTWSL JPWOLY DLYL ZABKPLK MVY SLAALY MYLXBLUJF AOL SLAALY AOHA JHTL BW TVZA VMALU DVBSK YLWYLZLUA L AOL ZLJVUK TVZA JVTTVU SLAALY DVBSK IL A HUK ZV VU IF DVYRPUN AOPZ VBA HUK MPSSPUN PU AOL SLAALYZ ZVTL DPSS MVYT VICPVBZ DVYKZ DPAO SLAALYZ TPZZPUN HSSVDPUN AOL JVKLIYLHRLY AV MPSS PU AOL NHWZ HUK YLJVCLY AOVZL SLAALYZ HZ DLSS JVUAHJA HUHSFZPZ HUVAOLY IHZPJ DLHWVU BZLK IF AOL JVKLIYLHRLY AHRLZ AOPZ WYPUJPWSL H ZALW MBYAOLY ZVTL SLAALYZ DPSS HWWLHY MYLXBLUASF HSVUNZPKL LHJO VAOLY AOL TVZA VICPVBZ LEHTWSL PU AOL LUNSPZO SHUNBHNL PZ AO HZ PU AOL VY AOHA IF JVTIPUPUN AOLZL ADV DLHWVUZ AOL JVKLIYLHRLY JVBSK THRL H YLHZVUHISL NBLZZ AOHA DOLYL H ZPUNSL SLAALY HWWLHYLK YLWLHALKSF HMALY AOL A DOPJO OL OHK HSYLHKF YLJVCLYLK MYVT SLAALY MYLXBLUJF AOL BURUVDU SLAALY DHZ WYVIHISF O WHYAPJBSHYSF PM AOL ULEA SLAALY OHK HSYLHKF ILLU YLJVCLYLK HZ L PU AOHA JHZL OL TPNOA JVUJSBKL AOHA AOL SLAALY HMALY AOL L DHZ WYVIHISF AOL ZAHYA VM H ULD DVYK HUK ZV AOL WYVJLZZ VM IBPSKPUN BW AOL TLZZHNL DVBSK NV VU'

wordcount={}
for word in text():
    if word not in wordcount:
        wordcount[word] = 1
    else:
        wordcount[word] += 1
for k,v in wordcount.items():
    print k, v
	

makeKey()	
