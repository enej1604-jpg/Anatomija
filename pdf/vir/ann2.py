ns={}; exec(open('ann1.py').read(), ns); SK=ns['A']['1-2']['p'][4]['a']
A={}
A['2-1']={'title':'Lobanja','p':[
 {'cap':'Kosti lobanje: os frontale, parietale, nasale, lacrimale, ethmoidale, sphenoidale, occipitale, temporale, zygomaticum, maxilla, mandibula.','a':SK},
 {'cap':'Lobanjsko dno od spodaj: foramen magnum, condyli occipitales, processus mastoideus, processus styloideus, os palatinum, processus pterygoideus.','a':[
  [45,8,'arcus alveolaris – zobni lok','k'],[50,16,'processus palatinus maxillae','k'],[51,29,'os palatinum','k'],[50,38,'vomer','k'],
  [57,43,'processus pterygoideus','k'],[34,48,'fossa mandibularis','s'],[42,58,'condylus occipitalis','s'],[50,62,'foramen magnum','k'],
  [64,55,'processus styloideus','k'],[72,62,'processus mastoideus','k'],[56,75,'os occipitale','k']]},
 {'cap':'Mandibula: corpus, ramus, angulus, processus coronoideus, processus condylaris; arcus zygomaticus.','a':[
  [32,25,'m. temporalis','m'],[22,57,'m. masseter','m'],[52,56,'arcus zygomaticus','k'],[48,78,'ramus mandibulae','k'],
  [84,52,'processus coronoideus','k'],[95,55,'processus condylaris','k'],[78,72,'corpus mandibulae','k'],[92,80,'angulus mandibulae','k']]},
 {'cap':'Čeljustni sklep: caput mandibulae v fossa mandibularis os temporale, discus articularis.','a':[
  [35,30,'squama ossis temporalis','k'],[41,45,'discus articularis','s'],[51,40,'tuberculum articulare','s'],[24,46,'capsula articularis','s'],
  [42,56,'caput mandibulae','s'],[40,73,'lig. stylomandibulare','s'],[62,45,'m. pterygoideus lateralis','m'],[68,65,'m. pterygoideus medialis','m']]},
]}
A['2-2']={'title':'Hrbtenica in prsni koš','p':[
 {'cap':'Hrbtenica od strani: vratna lordoza, prsna kifoza, ledvena lordoza; protuberantia occipitalis externa, processus spinosus C7.','a':[
  [57,19,'protuberantia occipitalis externa','k'],[61,27,'lordosis cervicalis – vratna','k'],[59,35,'proc. spinosus C7 (vertebra prominens)','k'],
  [60,52,'kyphosis thoracica – prsna','k'],[66,73,'lordosis lumbalis – ledvena','k'],[60,92,'os sacrum + os coccygis','k']]},
 {'cap':'Vratna vretenca: corpus, processus spinosus, processus articularis superior, processus transversus (tuberculum anterius/posterius), foramen transversarium.','a':[
  [50,10,'medulla spinalis','z'],[45,25,'n. spinalis','z'],[70,22,'nucleus pulposus','s'],[72,36,'discus intervertebralis (anulus)','s'],
  [38,52,'processus articularis superior','k'],[25,65,'processus spinosus','k'],[44,82,'tuberculum posterius','k'],[55,76,'foramen transversarium','k'],
  [62,80,'tuberculum anterius','k'],[74,62,'corpus vertebrae','k']]},
 {'cap':'Atlas in axis: dens axis, atlas (C1), axis (C2).','a':[
  [45,15,'os occipitale','k'],[24,42,'art. atlantooccipitalis','s'],[52,22,'clivus','k'],[56,48,'dens axis','k'],[66,43,'lig. alare','s'],
  [68,61,'atlas (C1)','k'],[72,86,'axis (C2)','k']]},
 {'cap':'Prsno vretence in rebro: fovea costalis superior/inferior, fovea costalis processus transversi; caput, collum, tuberculum costae.','a':[
  [55,10,'corpus T4 / T5','k'],[42,12,'fovea costalis inferior / superior','s'],[38,18,'fovea costalis processus transversi','s'],
  [36,35,'processus spinosus – dolg, navzdol','k'],[68,40,'costa V – rebro','k'],[86,37,'cartilago costalis','k'],
  [37,74,'processus transversus','k'],[64,75,'tuberculum costae','s'],[70,86,'collum costae','k'],[63,91,'caput costae','s'],[48,95,'corpus vertebrae','k']]},
 {'cap':'Prsni koš: rebra, rebrni hrustanci, sternum, prsna vretenca – spodaj prepona s kupolama in kraki.','a':[
  [50,25,'sternum – prsnica','k'],[30,22,'costae – rebra','k'],[37,45,'cartilago costalis','k'],[25,58,'diaphragma – desna kupola','m'],
  [78,56,'diaphragma – leva kupola','m'],[50,80,'crus dextrum','m'],[59,72,'crus sinistrum ob vretencih','m']]},
]}
A['2-3']={'title':'Ramenski obroč, zgornji ud, medenica, spodnji ud','p':[
 {'cap':'Scapula od spredaj: acromion, processus coracoideus, cavitas (fossa) glenoidalis, fossa subscapularis; humerus.','a':[
  [50,5,'acromion','k'],[45,12,'processus coracoideus','k'],[45,21,'cavitas glenoidalis','s'],[30,45,'fossa subscapularis','k'],
  [29,72,'tuberculum majus','k'],[33,77,'sulcus intertubercularis','k'],[40,70,'caput humeri','k'],[37,83,'collum chirurgicum','k'],[66,76,'collum anatomicum','k']]},
 {'cap':'Scapula od zadaj: spina scapulae, fossa supraspinata, fossa infraspinata; tuberculum majus humeri.','a':[
  [20,15,'lega m. supraspinatus','m'],[57,48,'clavicula','k'],[57,58,'m. supraspinatus','m'],[42,63,'fossa supraspinata – origo','k'],
  [62,63,'tuberculum majus – insertio','k'],[50,69,'spina scapulae','k'],[45,80,'fossa infraspinata','k']]},
 {'cap':'Komolec od spredaj: ulna in radius, sklepna ovojnica in vezi (lig. collaterale radiale/ulnare, lig. anulare radii), membrana interossea (chorda obliqua).','a':[
  [48,12,'humerus','k'],[66,30,'capsula articularis','s'],[32,42,'lig. collaterale radiale','s'],[69,46,'lig. collaterale ulnare','s'],
  [36,51,'lig. anulare radii','s'],[37,66,'tetiva m. biceps brachii','m'],[52,70,'chorda obliqua','s'],[35,92,'radius','k'],[56,92,'ulna','k']]},
 {'cap':'Zapestje: radius, ulna, ossa carpi (proksimalna in distalna vrsta); art. radiocarpea in art. mediocarpea.','a':[
  [30,30,'art. radiocarpea','s'],[72,20,'art. mediocarpea','s'],[55,55,'ossa metacarpalia I–V','k'],[63,63,'os trapezoideum','k'],[64,67,'os trapezium','k'],
  [57,68,'os capitatum','k'],[53,68,'os hamatum','k'],[49,72,'os pisiforme','k'],[50,77,'os triquetrum','k'],[55,79,'os lunatum','k'],[60,75,'os scaphoideum','k'],
  [61,92,'radius','k'],[48,93,'ulna','k']]},
 {'cap':'Roka: ossa carpi, ossa metacarpalia I–V, phalanges.','a':[
  [42,5,'ossa carpi','k'],[38,13,'art. carpometacarpea','s'],[64,58,'ossa metacarpalia','k'],[56,69,'art. metacarpophalangea','s'],
  [52,76,'phalanx proximalis','k'],[68,82,'phalanx media','k'],[67,94,'phalanx distalis','k']]},
 {'cap':'Medenica: os ilium, os sacrum, articulatio sacroiliaca.','a':[
  [13,25,'os ilium','k'],[29,28,'art. sacroiliaca','s'],[52,30,'os sacrum','k'],[52,58,'os coccygis','k'],[51,74,'symphysis pubica','s'],[56,86,'arcus pubicus','k']]},
 {'cap':'Medenica od spredaj: symphysis pubica, foramen obturatum, acetabulum.','a':[
  [20,25,'ala ossis ilii','k'],[50,45,'os sacrum – foramina sacralia','k'],[16,62,'acetabulum','s'],[62,66,'os pubis','k'],
  [50,72,'symphysis pubica','s'],[30,80,'foramen obturatum','k'],[34,95,'os ischii','k']]},
 {'cap':'Kolk: acetabulum, caput femoris, trochanter major, trochanter minor; vezi kolčnega sklepa.','a':[
  [50,10,'os ilium','k'],[44,36,'acetabulum','s'],[47,42,'caput femoris','s'],[30,52,'trochanter major','k'],[40,55,'lig. iliofemorale','s'],
  [62,55,'lig. pubofemorale','s'],[78,62,'membrana obturatoria','s'],[70,70,'os ischii','k'],[36,85,'femur','k'],[46,88,'trochanter minor','k']]},
 {'cap':'Tibia in fibula z membrana interossea cruris (levo za primerjavo ulna in radius).','a':[
  [36,40,'membrana interossea antebrachii','s'],[37,66,'ulna','k'],[31,77,'radius','k'],[61,12,'fibula','k'],[67,30,'tibia','k'],[63,46,'membrana interossea cruris','s']]},
 {'cap':'Kosti stopala: talus, calcaneus, os naviculare, os cuboideum, ossa cuneiformia; malleolus medialis et lateralis.','a':[
  [40,6,'fibula','k'],[55,8,'tibia','k'],[36,25,'malleolus lateralis','k'],[64,22,'malleolus medialis','k'],[54,32,'talus','k'],
  [55,40,'os naviculare','k'],[42,39,'calcaneus','k'],[52,57,'malleolus medialis','k'],[56,62,'talus','k'],[40,72,'os naviculare','k'],
  [32,72,'os cuneiforme mediale','k'],[52,76,'sustentaculum tali','k'],[62,85,'calcaneus','k'],[40,88,'aponeurosis plantaris','s']]},
]}
