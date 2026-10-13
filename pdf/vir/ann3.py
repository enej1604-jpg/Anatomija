A={}
A['3-1']={'title':'Hrustančevina','p':[
 {'cap':'Hialina hrustančevina – hondrociti v lakunah, homogena medceličnina.','a':[
  [51,50,'hondrocit v lakuni','t'],[32,51,'izogena skupina (2 celici)','t'],[45,28,'medceličnina – homogena','t']]},
 {'cap':'Kje je hrustanec v telesu: hialini (nos, grlo, rebra, sapnik, sklepi), elastični (uhelj, epiglotis), vezivni (medvretenčne ploščice, simfiza, meniskus).','a':[
  [34,13,'uhelj – elastični','t'],[41,13,'nos – hialini','t'],[45,22,'sklepni hrustanec – hialini','t'],[45,31,'rebrni hrustanci – hialini','t'],
  [36,36,'medvretenčna ploščica – vezivni','t'],[34,57,'simfiza – vezivni','t'],[30,79,'meniskus – vezivni','t'],
  [73,4,'epiglotis – elastični','t'],[73,9,'grlo – hialini','t'],[73,21,'sapnik – hialini','t']]},
 {'cap':'Hialini hrustanec: hondrociti, lakune, matriks (medceličnina).','a':[
  [62,20,'perihondrij','t'],[24,30,'hondrocit','t'],[57,40,'lakuna','t'],[36,72,'matriks – medceličnina','t']]},
 {'crop':[0,0,82,100],'cap':'Hialina hrustančevina: perihondrij (perichondrium), hondroblasti, izogene skupine (isogenous nest cells) hondrocitov.','a':[
  [40,22,'perichondrium – perihondrij','t'],[42,40,'hondroblasti (mladi)','t'],[45,70,'izogena skupina hondrocitov','t']]},
 {'cap':'Elastična hrustančevina – gosto mrežje elastičnih vlaken.','a':[
  [50,6,'perihondrij','t'],[40,32,'hondrociti v lakunah','t'],[62,45,'elastična vlakna – temna mreža','t']]},
 {'cap':'Vezivna hrustančevina – snopi kolagenskih vlaken tipa I, hondrociti v vrstah.','a':[
  [30,30,'kolagenska vlakna tipa I – snopi','t'],[40,50,'hondrociti v vrstah','t']]},
]}
ns={}; exec(open('ann2.py').read(), ns); VC=ns['A']['2-2']['p'][1]['a']
A['3-2']={'title':'Sklepi – zgradba in vrste','p':[
 {'cap':'Pravi (sinovijski) sklep: sklepna ovojnica (fibrozna plast + sinovijska membrana), sklepni hrustanec, sklepna votlina s tekočino, vezi.','a':[
  [33,14,'periosteum – pokostnica','k'],[32,27,'ligamentum – vez','s'],[29,42,'membrana fibrosa','s'],[42,45,'cavitas articularis','s'],
  [32,57,'membrana synovialis','s'],[42,53,'cartilago articularis','s'],[33,76,'substantia compacta','k'],
  [75,14,'femur','k'],[68,60,'corpus adiposum infrapatellare','o'],[86,53,'meniscus','s'],[75,82,'tibia','k']]},
 {'cap':'Sklepna ovojnica, sinovijska membrana, sklepni hrustanec.','a':[
  [42,22,'kost – epifiza','k'],[38,50,'cartilago articularis','s'],[79,40,'membrana synovialis','s'],[80,55,'capsula articularis','s'],
  [68,63,'cavitas articularis – sinovijska tekočina','s']]},
 {'cap':'Vratna vretenca: medvretenčna plošča (nucleus pulposus, anulus), hrbtenjača in spinalni živec, foramen transversarium, processus spinosus in articularis.','a':VC},
 {'cap':'Fibrozni sklepi: sutura (lobanjski šiv), sindezmoza (membrana interossea med radiusom in ulno).','a':[
  [50,10,'sutura – lobanjski šiv','s'],[40,22,'diploë – gobasta kost','k'],[55,25,'substantia compacta','k'],[25,51,'sutura coronalis','s'],
  [79,40,'ulna','k'],[76,48,'radius','k'],[80,62,'membrana interossea – syndesmosis','s']]},
 {'cap':'Hrustančni sklepi: primarni (epifizna ploščica) in sekundarni (medvretenčna ploščica).','a':[
  [30,29,'cartilago articularis','s'],[22,33,'caput femoris','k'],[26,42,'epifizna ploščica – synchondrosis','s'],[16,62,'femur','k'],
  [70,17,'discus intervertebralis – symphysis','s'],[68,40,'corpus vertebrae','k']]},
 {'cap':'Pregled tipov sinovijskih sklepov v telesu.','a':[
  [65,11,'art. acromioclavicularis – ravni sklep','s'],[63,35,'art. cubiti – tečajasti sklep','s'],[25,41,'art. atlantoaxialis – vrtljivi sklep','s'],
  [62,50,'art. carpometacarpea pollicis – sedlasti','s'],[57,66,'art. metacarpophalangea – jajčasti (elipsoidni)','s'],[35,71,'art. coxae – kroglasti sklep','s']]},
]}
A['3-3']={'title':'Tipi sklepov po oseh','p':[
 {'cap':'Kroglasti (articulatio spheroidea) – triaksialni: rama, kolk. Shema: 1 kroglasti, 2 jajčasti, 3 sedlasti, 4 tečajasti, 5 čepasti.','a':[
  [35,10,'1 · kroglasti – 3 osi (rama, kolk)','s'],[55,12,'2 · jajčasti – 2 osi','s'],[73,12,'3 · sedlasti – 2 osi','s'],
  [42,35,'4 · tečajasti – 1 os','s'],[67,38,'5 · čepasti – 1 os (rotacija)','s'],[28,72,'capsula fibrosa','s'],[35,80,'caput humeri v cavitas glenoidalis','s']]},
 {'cap':'Jajčasti (articulatio condylaris) – biaksialni: atlantookcipitalni, radiokarpalni, MCP.','a':[
  [57,15,'2 · jajčasti (elipsoidni) sklep','s'],[67,71,'A · art. atlantooccipitalis – jajčasti','s'],[66,80,'B · art. atlantoaxialis – čepasti','s']]},
 {'cap':'Sedlasti (articulatio sellaris) – CMC palca; tečajasti (ginglymus) – komolec, IP, gleženj, koleno.','a':[
  [73,13,'3 · sedlasti – CMC palca','s'],[38,42,'4 · tečajasti – komolec, IP, gleženj','s'],[28,73,'art. patellofemoralis','s'],[37,79,'art. tibiofemoralis','s'],
  [65,68,'art. radioulnaris proximalis','s'],[68,82,'membrana interossea','s'],[66,92,'art. radioulnaris distalis','s']]},
 {'cap':'Čepasti (articulatio trochoidea) – atlantoaksialni, radioulnarni: rotacija.','a':[
  [17,25,'1 · kroglasti','s'],[47,25,'2 · jajčasti','s'],[78,22,'3 · sedlasti','s'],[22,75,'4 · tečajasti','s'],[68,82,'5 · čepasti – rotacija okoli ene osi','s']]},
]}
TMJ=ns['A']['2-1']['p'][3]['a']; AA=ns['A']['2-2']['p'][2]['a']; RIB=ns['A']['2-2']['p'][3]['a']
A['3-4']={'title':'Sklepi glave in trupa','p':[
 {'cap':'Articulatio temporomandibularis: caput mandibulae, fossa mandibularis, discus articularis.','a':TMJ},
 {'cap':'Zgornja vratna sklepa od zadaj (odprt vretenčni kanal): lig. transversum atlantis, ligg. alaria, membrana tectoria, sklepni ovojnici.','a':[
  [50,15,'os occipitale – pars basilaris','k'],[30,45,'capsula art. atlantooccipitalis','s'],[62,37,'ligg. alaria','s'],[50,47,'lig. transversum atlantis','s'],
  [45,58,'lig. cruciforme atlantis','s'],[24,55,'atlas','k'],[60,63,'membrana tectoria','s'],[70,60,'capsula art. atlantoaxialis','s'],[32,80,'axis','k']]},
 {'cap':'Dens axis z vezmi: lig. apicis dentis, ligg. alaria; articulatio atlantooccipitalis, atlas, axis.','a':AA+[[50,30,'lig. apicis dentis','s']]},
 {'cap':'Disci intervertebrales; lig. longitudinale anterius et posterius.','a':[
  [12,40,'lig. longitudinale anterius','s'],[21,30,'discus intervertebralis','s'],[79,30,'lig. longitudinale posterius','s'],[72,28,'discus intervertebralis','s']]},
 {'cap':'Kratke vezi hrbtenice: ligamenta flava, interspinalia, intertransversaria.','a':[
  [10,27,'foramen intervertebrale','k'],[30,32,'discus intervertebralis','s'],[15,72,'ligamenta flava','s'],[36,75,'lig. flavum (stransko)','s'],
  [80,30,'lig. longitudinale anterius','s'],[87,36,'lig. longitudinale posterius','s'],[81,45,'lig. flavum','s'],[79,53,'lig. intertransversarium','s'],
  [92,57,'lig. supraspinale','s'],[90,63,'lig. interspinale','s']]},
 {'cap':'Sklepa rebra z vretencem: glavica rebra – foveae costales; tuberculum costae – processus transversus.','a':RIB},
]}
P23=ns['A']['2-3']['p']
A['3-5']={'title':'Sklepi ramenskega obroča in zgornjega uda','p':[
 {'cap':'Articulatio sternoclavicularis: discus articularis, lig. sternoclaviculare, lig. costoclaviculare.','a':[
  [24,15,'clavicula','k'],[40,22,'discus articularis','s'],[56,30,'lig. interclaviculare','s'],[18,38,'capsula articularis','s'],
  [22,33,'lig. costoclaviculare','s'],[25,51,'cartilago costalis I','k'],[45,58,'manubrium sterni','k'],[75,46,'lig. sternoclaviculare','s'],[72,70,'lig. sternocostale radiatum','s']]},
 {'cap':'Articulatio acromioclavicularis – lig. acromioclaviculare.','a':[
  [43,9,'art. acromioclavicularis','s'],[70,8,'clavicula','k'],[42,20,'art. humeri','s'],[65,40,'scapula','k'],[35,55,'humerus','k']]},
 {'cap':'Articulatio humeroscapularis: cavitas glenoidalis, caput humeri, lig. coracohumerale, lig. coracoacromiale.','a':[
  [33,15,'clavicula','k'],[38,23,'tetiva m. supraspinatus','m'],[40,30,'labrum glenoidale','s'],[40,38,'cavitas glenoidalis','s'],
  [40,56,'membrana synovialis','s'],[40,66,'membrana fibrosa','s'],[60,18,'acromion','k'],[55,22,'lig. coracoacromiale','s'],[56,27,'bursa subacromialis','s'],
  [66,42,'capsula articularis','s'],[67,52,'tetiva caput longum m. biceps brachii','m'],[52,46,'caput humeri','k'],[52,80,'humerus','k']]},
 {'cap':'Articulatio cubiti – komolec (pogled z medialne strani: ovojnica in kolateralna vez).','a':[
  [20,30,'humerus','k'],[22,62,'capsula articularis','s'],[45,66,'lig. collaterale ulnare','s'],[17,72,'olecranon ulnae','k']]},
 {'cap':'Radioulnarna sklepa in membrana interossea antebrachii; lig. anulare radii.','a':P23[2]['a']},
 {'cap':'Articulatio radiocarpalis in mediocarpalis.','a':P23[3]['a']},
 {'cap':'Sklepi roke: CMC, MCP, IP.','a':[
  [38,10,'art. carpometacarpea (CMC)','s'],[56,69,'art. metacarpophalangea (MCP)','s'],[52,85,'art. interphalangea proximalis (PIP)','s'],
  [67,94,'art. interphalangea distalis (DIP)','s'],[48,58,'MCP palca','s']]},
]}
A['3-6']={'title':'Sklepi medenice in spodnjega uda','p':[
 {'cap':'Articulatio sacroiliaca (sacroiliac joint): ilium – sacrum.','a':P23[5]['a']},
 {'cap':'Symphysis pubica.','a':P23[6]['a']},
 {'cap':'Articulatio coxae: acetabulum, caput femoris, lig. iliofemorale, ischiofemorale, pubofemorale, lig. capitis femoris.','a':P23[7]['a']},
 {'cap':'Articulatio genus: menisci, lig. cruciatum anterius/posterius, lig. collaterale mediale/laterale, lig. patellae.','a':[
  [45,10,'femur','k'],[50,28,'menisci','s'],[47,42,'tibia','k'],[41,42,'fibula','k'],[55,63,'lig. patellae','s'],[46,71,'lig. transversum genus','s'],
  [36,78,'meniscus medialis','s'],[47,86,'lig. cruciatum anterius','s'],[52,94,'lig. cruciatum posterius','s'],[66,88,'meniscus lateralis','s']]},
 {'cap':'Meniski in križni vezi (intraartikularne strukture).','a':[
  [15,25,'meniski in križni vezi v kolenu','s'],[72,55,'lig. cruciatum anterius / posterius','s']]},
 {'cap':'Articulatio tibiofibularis, membrana interossea cruris.','a':P23[8]['a']},
 {'cap':'Articulatio talocruralis in vezi gležnja.','a':P23[9]['a']},
 {'cap':'Articulatio talocalcaneonavicularis in vezi stopala.','a':[
  [60,15,'tibia','k'],[52,40,'lig. deltoideum (mediale)','s'],[35,56,'os naviculare','k'],[71,48,'lig. talotibiale posterius','s'],
  [45,80,'lig. calcaneonaviculare plantare','s'],[60,86,'lig. plantare longum','s'],[76,80,'calcaneus','k']]},
]}
A['3-7']={'title':'Mišično tkivo','p':[
 {'cap':'Zgradba mišice: mišično vlakno, endomizij, fascikel (perimizij), epimizij, fascija, kita, kost.','a':[
  [40,30,'epimysium','m'],[64,16,'perimysium','m'],[67,29,'krvna žila','z'],[73,37,'mišično vlakno (myocytus)','m'],
  [62,42,'fasciculus – snop vlaken','m'],[62,57,'endomysium','m'],[16,70,'tendo – kita','s'],[18,90,'os – kost','k']]},
 {'cap':'Deli mišice: origo (caput), venter, cauda, tendo – insertio; fascija.','a':[
  [50,20,'caput – glava (origo)','m'],[46,45,'fascia – ovojnica','m'],[52,52,'venter – trebuh','m'],[50,82,'cauda – rep','m'],[50,94,'tendo – kita (insertio)','s']]},
 {'cap':'Večglave mišice (dvoglava, troglava) s kitami; pomožni aparat: kita, aponevroza, kitna ovojnica, sluzne vrečke.','a':[
  [33,22,'dvoglava mišica – 2 glavi','m'],[40,55,'skupni trebuh','m'],[33,88,'tendo – kita','s'],[66,18,'troglava mišica – 3 glave','m'],[68,85,'tendo – kita','s']]},
 {'cap':'Skeletno mišično vlakno: sarkolema, jedra, miofibrile, sarkoplazemski retikulum, sarkomera (pas A, I, H, črti Z in M).','a':[
  [30,13,'nucleus – jedra ob robu','m'],[20,22,'pas I – svetel','m'],[38,33,'pas A – temen','m'],[61,12,'mitohondrij','t'],[63,18,'sarcolemma','m'],
  [67,26,'myofibrilla','m'],[20,68,'sarkoplazemski retikulum','m'],[30,72,'aktin – tanki filament','m'],[37,70,'črta Z','m'],
  [50,61,'sarkomera (Z–Z)','m'],[51,70,'pas H','m'],[79,70,'miozin – debeli filament','m'],[79,88,'črta M','m']]},
 {'cap':'Sarkomera: črta Z, pas I, pas A, pas H, črta M; tanki (aktinski) in debeli (miozinski) filamenti.','a':[
  [40,9,'sarkomera = Z do Z','m'],[28,40,'črta Z','m'],[25,64,'tanki filament – aktin','m'],[49,58,'črta M','m'],
  [60,62,'debeli filament – miozin','m'],[50,82,'pas H (samo miozin)','m'],[26,90,'pas I (samo aktin)','m'],[60,92,'pas A (dolžina miozina)','m']]},
 {'cap':'Tanki filament: aktin, tropomiozin, troponin.','a':[
  [40,62,'aktinski filamenti','m'],[62,58,'miozin II','m'],[55,83,'plazmalema','t'],[22,85,'integrini','t']]},
 {'cap':'Miozin – debeli filament; pri krčenju aktin zdrsne ob miozinu (A–B se ne spremeni, sarkomera se skrajša).','a':[
  [30,19,'aktin – tanki','m'],[56,22,'miozin – debeli (glavice)','m'],[10,30,'sproščeno – črta Z','m'],[20,70,'skrčeno – Z se približata','m']]},
 {'cap':'Motorična ploščica: akson motoričnega nevrona, vezikli z nevrotransmitorjem, sinaptična reža, receptorji.','a':[
  [60,5,'mielin','z'],[52,15,'akson motoričnega nevrona','z'],[44,38,'vezikli z acetilholinom','z'],[66,40,'mitohondriji','t'],
  [30,51,'sinaptična reža','z'],[24,60,'motorična ploščica','z'],[66,57,'receptorji za nevrotransmitor','z'],[35,76,'skeletno mišično vlakno','m']]},
 {'cap':'Srčna mišičnina – kardiomiociti, interkalarne ploščice.','a':[
  [52,44,'disci intercalares – interkalarne ploščice','m'],[38,70,'centralno jedro','m'],[66,82,'razvejana vlakna','m']]},
 {'cap':'Gladka mišičnina – vretenaste celice.','a':[
  [40,40,'vretenaste gladke mišične celice','m'],[62,30,'podolgovato jedro v sredini','m']]},
 {'cap':'Od mišice do sarkomere: mišica → snop → mišično vlakno → miofibrila → sarkomera (aktin, miozin).','a':[
  [20,18,'tendo – kita','s'],[40,16,'musculus – mišica','m'],[65,22,'fasciculus – snop','m'],[76,30,'mišično vlakno','m'],[82,36,'myofibrilla','m'],
  [45,70,'črta Z','m'],[63,72,'črta M','m'],[55,85,'sarkomera','m'],[78,82,'aktin','m'],[80,86,'miozin','m']]},
 {'cap':'Agonist, antagonist, sinergist (biceps – triceps – brachialis).','a':[
  [41,25,'m. biceps brachii – agonist','m'],[36,49,'m. brachioradialis – sinergist','m'],[86,49,'m. biceps brachii','m'],[85,66,'m. brachialis – sinergist','m']]},
 {'cap':'Mišica: trebuh (muscle belly), kita (tendon), sklepna ovojnica in vezi, hrustanec, kost.','a':[
  [37,58,'tendo – kita (origo)','s'],[48,48,'venter – trebuh mišice','m'],[63,44,'tendo – kita (insertio)','s'],[66,55,'kost','k'],
  [50,70,'sklepna ovojnica in vezi','s'],[58,70,'sklepni hrustanec','s']]},
]}
P21=ns['A']['2-1']['p']
A['3-8']={'title':'Mišice glave in vratu','p':[
 {'cap':'Mišice glave – anterolateralno; narastišča mišic na lobanji.','a':[
  [35,16,'m. occipitofrontalis','m'],[28,30,'m. orbicularis oculi','m'],[52,30,'m. temporalis','m'],[33,63,'m. buccinator','m'],
  [30,72,'m. orbicularis oris','m'],[45,58,'m. masseter','m'],[77,52,'narastišče m. sternocleidomastoideus','m']]},
 {'cap':'Lobanjsko dno (inferiorni pogled) – kostne točke in narastišča mišic.','a':P21[1]['a']},
 {'cap':'M. temporalis – fossa temporalis → processus coronoideus.','a':[
  [30,25,'m. temporalis','m'],[28,48,'art. temporomandibularis','s'],[17,72,'m. masseter','m'],[60,68,'fossa temporalis – origo','k'],
  [77,60,'processus condylaris','k'],[86,64,'processus coronoideus – insertio','k'],[77,82,'ramus mandibulae','k'],[77,92,'angulus mandibulae','k']]},
 {'cap':'M. masseter – arcus zygomaticus → tuberositas masseterica (angulus mandibulae).','a':P21[2]['a']},
 {'cap':'M. pterygoideus lateralis – sklepni disk, collum mandibulae.','a':[
  [45,17,'m. pterygoideus lateralis','m'],[30,30,'m. pterygoideus medialis','m'],[25,58,'processus coronoideus','k'],[41,62,'fovea pterygoidea – insertio','k'],
  [45,72,'collum mandibulae','k'],[66,62,'m. pterygoideus lateralis (zeleno)','m'],[60,76,'m. pterygoideus medialis','m']]},
 {'cap':'M. pterygoideus medialis – tuberositas pterygoidea (notranja stran angulus mandibulae).','a':[
  [50,30,'m. pterygoideus medialis','m'],[62,62,'m. pterygoideus lateralis','m'],[60,76,'m. pterygoideus medialis','m'],[37,82,'angulus – tuberositas pterygoidea','k']]},
 {'cap':'Mimične mišice: frontalis, temporalis, orbicularis oculi, levator labii sup., zygomaticus, masseter, buccinator, risorius, procerus, corrugator supercilii, nasalis, orbicularis oris, depressor anguli oris, platysma, depressor labii inf.','a':[
  [36,22,'m. frontalis – dvig obrvi','m'],[32,35,'m. orbicularis oculi – zapiranje očesa','m'],[38,44,'m. levator labii superioris','m'],
  [35,51,'m. zygomaticus major – nasmeh','m'],[36,59,'m. buccinator – pihanje','m'],[36,66,'m. risorius','m'],
  [47,30,'m. procerus','m'],[45,27,'m. corrugator supercilii – mrščenje','m'],[54,40,'m. nasalis','m'],[53,54,'m. orbicularis oris – zapiranje ust','m'],
  [56,61,'m. depressor anguli oris','m'],[51,64,'m. depressor labii inferioris','m']]},
 {'cap':'M. buccinator – lična mišica (od raphe pterygomandibularis do ustnega kota).','a':[
  [20,52,'m. buccinator','m'],[15,65,'raphe pterygomandibularis','s'],[18,72,'m. constrictor pharyngis superior','m'],[80,75,'m. buccinator','m']]},
 {'cap':'Sprednje vratne mišice: supra- in infrahioidne, SCM, scaleni.','a':[
  [52,10,'m. stylohyoideus','m'],[56,16,'m. digastricus','m'],[42,30,'os hyoideum','k'],[50,32,'m. thyrohyoideus','m'],[40,38,'cartilago thyroidea','o'],
  [43,45,'m. sternohyoideus','m'],[55,42,'m. omohyoideus','m'],[15,47,'mm. scaleni','m'],[25,56,'m. sternocleidomastoideus','m'],[62,55,'m. trapezius','m']]},
 {'cap':'Vrat lateralno: splenius, levator scapulae, scaleni, SCM, trapezius, digastricus, plexus brachialis.','a':[
  [40,35,'m. splenius','m'],[40,45,'m. levator scapulae','m'],[36,53,'mm. scaleni (ant., med., post.)','m'],[25,72,'m. trapezius','m'],
  [60,52,'m. digastricus','m'],[56,62,'m. sternocleidomastoideus','m'],[40,79,'plexus brachialis','z']]},
 {'cap':'Mimične mišice: corrugator supercilii, levator labii sup. alaeque nasi, levator labii sup., buccinator, depressor labii inf., mentalis.','a':[
  [56,31,'mršči obrvi','m'],[60,45,'dviga ustnico in nosnico','m'],[57,50,'dviga zgornjo ustnico','m'],[57,65,'stiska lice ob zobe','m'],
  [61,73,'spušča spodnjo ustnico','m'],[63,77,'nabira kožo brade','m']]},
]}
