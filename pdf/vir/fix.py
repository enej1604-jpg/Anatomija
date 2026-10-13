# Corrected label positions: FIX[plate][panel] = list of [x%, y%, label, cat]  or dict(a=..., cap=..., skip=True)
FIX={}
def f(plate,k,a=None,**kw):
    d=FIX.setdefault(plate,{}); e=dict(kw)
    if a is not None: e['a']=a
    d[k]=e
f('1-1',1,[[40,25,'planum frontale – čelna (koronalna) ravnina','r'],[36,40,'planum horizontale – vodoravna ravnina','r'],[60,15,'planum medianum – srednja sagitalna ravnina','r'],
 [43,10,'medialis ↔ lateralis','r'],[58,30,'superior (cranialis) ↔ inferior (caudalis)','r'],[57,60,'proximalis ↔ distalis','r'],[47,82,'posterior ↔ anterior','r'],[55,84,'dexter ↔ sinister','r']])
f('1-1',2,[[22,22,'superior / cranialis','r'],[17,33,'posterior / dorsalis','r'],[21,50,'inferior / caudalis','r'],[29,45,'anterior / ventralis','r'],
 [64,35,'proximalis','r'],[61,47,'distalis','r'],[70,8,'planum medianum','r'],[78,30,'planum sagittale','r'],[66,45,'planum horizontale','r'],
 [72,77,'medialis','r'],[72,87,'lateralis','r'],[57,63,'radialis ↔ ulnaris','r'],[20,75,'planum horizontale (transversale)','r'],[24,90,'planum frontale (coronale)','r']])
f('1-1',3,[[15,10,'palmaris (volaris) – dlan','r'],[19,31,'dorsalis – hrbtišče dlani','r'],[7,28,'proximalis','r'],[29,17,'distalis','r'],
 [85,7,'dorsalis pedis – hrbtišče stopala','r'],[66,32,'plantaris – podplat','r'],[67,12,'distalis (stopalo)','r'],[82,33,'proximalis (stopalo)','r'],
 [35,72,'n. medianus – koža dlani (radialni 3½ prsta)','z'],[31,80,'n. ulnaris – koža mezinca','z'],[47,76,'n. radialis – hrbtišče roke','z']])
f('1-2',1,[[12,24,'abductio – odmik','r'],[14,37,'adductio – primik','r'],[57,22,'flexio – upogib','r'],[52,38,'extensio – izteg','r'],
 [84,28,'adductio horizontalis (horizontalna fleksija)','r'],[86,57,'abductio horizontalis (horizontalna ekstenzija)','r'],[10,66,'rotatio externa – zunanja rotacija','r'],[27,69,'rotatio interna – notranja rotacija','r']])
f('1-2',2,[[11,18,'retractio – pomik nazaj','r'],[37,18,'protractio – pomik naprej','r'],[17,62,'elevatio – dvig','r'],[37,66,'depressio – spust','r'],
 [73,40,'protractio mandibulae','r'],[75,72,'retractio mandibulae','r']])
f('1-2',3,[[32,20,'flexio v ramenskem sklepu','r'],[11,65,'flexio v kolčnem sklepu','r'],[68,23,'extensio v ramenskem sklepu','r'],[84,79,'extensio v kolčnem sklepu','r']])
f('1-2',4,[[5,20,'extensio zapestja','r'],[4,37,'flexio zapestja','r'],[5,72,'extensio / flexio prstov','r'],[76,15,'flexio / extensio komolca','r'],
 [50,90,'flexio / extensio kolena','r'],[93,67,'flexio dorsalis (dorzalna fleksija)','r'],[96,84,'flexio plantaris (plantarna fleksija)','r']])
f('1-2',5,[[20,22,'os frontale – čelnica','k'],[45,18,'os parietale – temenica','k'],[9,47,'os nasale – nosnica','k'],[17,47,'os lacrimale – solznica','k'],
 [20.5,44,'os ethmoidale – rešetnica (medialna stena očnice)','k'],[25,45,'os sphenoidale – zagozdnica (veliko krilo)','k'],[66,55,'os occipitale – zatilnica','k'],
 [45,55,'os temporale – senčnica','k'],[18,58,'os zygomaticum – ličnica','k'],[12,64,'maxilla – zgornja čeljust','k'],[22,88,'mandibula – spodnja čeljust','k']])
f('1-3',1,cap='Živalska celica in organeli. Pozor: napis »celična stena« na sliki je napaka – živalske celice nimajo celične stene; zunanja plast je celična membrana.',a=[
 [29,26,'apparatus Golgi – Golgijev aparat','t'],[20,35,'cytoplasma – citoplazma','t'],[33,60,'reticulum endoplasmaticum granulosum – zrnati ER','t'],
 [41,45,'nucleus – jedro (DNK)','t'],[54,33,'vacuola – vakuola','t'],[55,57,'mitochondrion – mitohondrij','t'],[24,60,'membrana cellularis – celična membrana','t'],
 [56,17,'cytoskeleton – celično ogrodje','t'],[46,16,'mitochondrion (prerez)','t']])
f('1-3',2,[[12,38,'C · nucleus – jedro','t'],[16,51,'B · reticulum endoplasmaticum','t'],[7,60,'cytoplasma – citoplazma','t'],[18,74,'D · mitochondrion','t'],[20,87,'A · membrana cellularis','t']])
f('1-3',3,[[25,22,'mitochondrion – kriste notranje membrane (tvorba ATP)','t'],[84,31,'mala podenota ribosoma','t'],[63,29,'mRNA','t'],[70,42,'velika podenota ribosoma','t'],
 [81,49,'nastajajoča beljakovinska veriga','t'],[17,66,'cisterne Golgijevega aparata','t'],[26,59,'cis stran – prihajajoči mešički','t'],[35,86,'trans stran – sekretorni mešiček','t']])
f('1-3',4,cap='Lizosomi (prebavni mešički s kislimi hidrolazami) in centrosom (dve centrioli, iz katerih izraščajo mikrotubuli).',a=[
 [28,22,'membrana lysosomae – membrana lizosoma','t'],[35,27,'prebavni encimi in kislina','t'],[27,37,'delno razgrajen organel','t'],[76,27,'lysosoma – lizosom v celici','t'],
 [52,67,'centriolum (materinska)','t'],[51,73,'centriolum (hčerinska)','t'],[61,52,'microtubuli – mikrotubuli','t']])
f('1-3',5,cap='Celična membrana: dvosloj fosfolipidov s holesterolom in beljakovinami; na zunanji strani verige ogljikovih hidratov (glikokaliks).',a=[
 [24,56,'dvosloj fosfolipidov','t'],[47,59,'holesterol','t'],[63,33,'verige ogljikovih hidratov (glikoprotein)','t'],[35,44,'zunanjost celice','o'],
 [68,60,'integralna beljakovina','t'],[61,74,'periferna beljakovina','t'],[38,86,'notranjost celice – citoplazma','o']])
f('1-3',6,cap='A olajšana difuzija – s transportno beljakovino, v smeri koncentracijskega gradienta, brez ATP. B aktivni prenos – proti gradientu, porablja ATP.',a=[
 [23,22,'koncentracijski gradient (visoka → nizka)','t'],[31,13,'molekula snovi','t'],[30,25,'transportna beljakovina','t'],[38,21,'vezavno mesto','t'],
 [77,35,'A · olajšana difuzija – snov preide navzdol po gradientu','t'],[32,77,'ATP','t'],[74,73,'ADP + fosfat','t'],[71,77,'B · aktivni prenos – ion proti gradientu','t']])
f('1-4',1,[[24,21,'cilia – migetalke','t'],[67,25,'microvilli – mikrovili','t'],[67,43,'zonula occludens – tesni stik','s'],[67,48,'zonula adherens – priležni pas','s'],
 [67,51,'desmosoma – dezmosom','s'],[67,58,'nexus – presledkovni stik','s'],[60,73,'lamina basalis','t'],[60,79,'retikularna vlakna (lamina reticularis)','t'],
 [26,59,'jedro epitelijske celice','t'],[12,82,'vezivo pod epitelijem','t'],[30,78,'živčni končič','z'],[55,88,'kapilara','z']])
f('1-4',2,[[20,29,'a · priležni stik – beljakovinski filamenti','s'],[16,62,'b · tesni stik – zlepljeni membrani','s'],[20,74,'beljakovine tesnega stika','s'],
 [60,80,'c · presledkovni stik – beljakovinski kanali','s'],[60,54,'jedro','t'],[70,61,'bazalna membrana','t'],[50,47,'medcelični prostor','o']])
f('1-4',3,[[18,12,'apikalna (prosta) površina','t'],[34,22,'lateralne površine','t'],[29,52,'bazalna površina','t'],
 [45,55,'lamina basalis','t'],[45,62,'lamina reticularis','t'],[45,70,'vezivo','t'],[16,74,'živec','z'],[29,82,'krvna žila','z']])
f('1-4',4,[[45,22,'ploščata celica (pogled od zgoraj)','t'],[51,46,'sploščeno jedro','t'],[30,61,'ena sama plast celic','t'],[50,92,'bazalna membrana','t']])
f('1-4',5,[[30,25,'apikalna površina','t'],[24,47,'izoprizmatske celice – ena plast','t'],[44,46,'okroglo jedro v sredini celice','t'],
 [55,54,'bazalna membrana','t'],[52,64,'lamina propria (vezivo)','t'],[43,61,'kapilara','z']])
f('1-4',6,[[13,27,'cilia – migetalke','t'],[63,15,'terminal bars – stiki med celicami','s'],[30,40,'visokoprizmatska celica','t'],[41,52,'podolgovato jedro','t'],
 [50,69,'bazalna membrana','t'],[50,76,'lamina propria','t'],[35,74,'kapilara','z']])
f('1-4',7,[[40,7,'površinske ploščate celice','t'],[50,33,'srednje plasti','t'],[40,57,'bazalna plast – celice se delijo','t'],[60,67,'bazalna membrana','t']])
f('1-4',9,cap='Eksokrine žleze po načinu izločanja: (a) merokrino – eksocitoza, celica ostane cela (slinavka); (b) apokrino – odščipne se vrh celice (mlečna žleza); (c) holokrino – celica razpade in postane izloček (lojnica).',a=[
 [30,21,'glandula salivaria – slinavka','o'],[51,3,'izloček (eksocitoza)','t'],[60,6,'sekretorni mešiček','t'],[57,16,'Golgijev aparat','t'],
 [30,46,'glandula mammaria – mlečna žleza','o'],[64,38,'odščipnjen vrh celice = izloček','t'],[30,77,'glandula sebacea – lojnica','o'],
 [62,70,'zrela celica razpade → izloček','t'],[61,84,'delitev nadomesti izgubljeno celico','t']])
f('1-4',10,cap='Endokrine žleze – nimajo izvodil, hormoni gredo neposredno v kri.',a=[
 [23,24,'glandula suprarenalis – nadledvičnica (na ledvici)','o'],[50,25,'hypophysis – hipofiza','o'],[74,33,'corpus pineale – češerika','o'],[17,54,'thymus – priželjc','o'],
 [23,77,'glandula thyroidea – ščitnica','o'],[50,91,'pancreas – trebušna slinavka','o'],[82,55,'testis – mod','o'],[76,74,'ovarium – jajčnik','o']])
f('1-5',1,cap='Fibroblast – glavna celica veziva; sintetizira kolagenska vlakna in osnovno snov (zato veliko zrnatega ER in Golgijev aparat).',a=[
 [47,47,'nucleus – jedro','t'],[42,60,'zrnati endoplazemski retikulum','t'],[49,30,'Golgijev aparat','t'],[56,59,'mitohondrij','t'],
 [36,72,'kolagenska vlakna (fibrile)','t'],[52,16,'sekretorni mešički','t'],[69,66,'citoplazma','t'],[71,77,'izrastki celice','t']])
f('1-5',2,cap='Mezenhimska matična celica se diferencira v osteoblast (→ kost), hondrocit (→ hrustanec), fibroblast (→ vezivo) in adipocit (→ maščevje).',a=[
 [48,15,'mezenhimska matična celica','t'],[14,39,'osteoblast','t'],[13,66,'osteocit → kost','t'],[40,62,'hondrocit → hrustanec','t'],
 [60,65,'fibroblast → vezivo','t'],[85,61,'adipocit → maščevje','t']])
f('1-5',3,[[22,29,'zrnca melanina','t'],[32,62,'melanosom','t'],[43,72,'Golgijev aparat','t'],[52,73,'jedro','t'],[56,79,'zrnati ER','t'],[48,84,'mitohondrij','t'],
 [59,38,'dendriti – izrastki, ki melanin oddajo keratinocitom','t']])
f('1-5',4,cap='Histiocit (tkivni makrofag) – fagocitna celica veziva, nastane iz monocita; ob njem eritrociti za primerjavo velikosti.',a=[[52,45,'jedro histiocita','t'],[38,40,'citoplazma – fagocitoza','t'],[59,22,'eritrocit','z']])
f('1-5',5,cap='Tkivni bazofilec (mastocit) – zrnca s histaminom in heparinom; sproščanje pri vnetju in alergiji.',a=[[55,20,'metakromatična zrnca (histamin, heparin)','t'],[58,58,'jedro','t'],[22,55,'celična membrana','t']])
f('1-5',6,cap='Nevtrofilni granulocit – jedro iz 3–5 segmentov; prva obramba pri bakterijskem vnetju.',a=[[58,40,'segmentirano jedro','t'],[35,72,'citoplazma','t']])
f('1-5',7,cap='Rahlo vezivo: kolagenska vlakna (debela, rožnata, valovita) in elastična vlakna (tanka, temna, razvejana).',a=[[18,24,'kolagenska vlakna – debela, rožnata','t'],[70,80,'kolagensko vlakno','t'],[40,51,'elastična vlakna – tanka, razvejana','t'],[56,62,'elastično vlakno','t']])
f('1-5',8,cap='Retikulinska vlakna (impregnacija s srebrom – črna) tvorijo mrežo, ki nosi celice v krvotvornih in limfatičnih organih.',a=[[42,41,'retikulinska vlakna – črna mreža','t'],[50,68,'retikulinsko vlakno','t'],[62,52,'celice med vlakni','t']])
f('1-5',9,cap='Čvrsto urejeno vezivo (kita): vzporedna kolagenska vlakna, med njimi vrste sploščenih fibroblastov.',a=[[33,21,'jedro fibroblasta','t'],[66,36,'fibroblast med vlakni','t'],[80,15,'kolagenska vlakna – vzporedna','t']])
f('1-6',1,cap='Zgradba kože: povrhnjica (epidermis), usnjica (dermis), podkožje (tela subcutanea) z dlako, žlezami in čutnicami.',a=[
 [25,25,'epidermis – povrhnjica','t'],[22,50,'dermis – usnjica','t'],[24,74,'tela subcutanea – podkožje','t'],[38,48,'Meissnerjevo telesce – čutnica za dotik','z'],
 [45,81,'Pacinijevo telesce – čutnica za pritisk','z'],[36,52,'prosti živčni končiči – bolečina, temperatura','z'],[56,20,'pilus – dlaka','o'],
 [62,54,'glandula sebacea – lojnica','o'],[68,50,'m. arrector pili – mišica, ki dvigne dlako','m'],[55,77,'glandula sudorifera – znojnica','o']])
f('1-6',2,[[46,22,'pilus – dlaka','o'],[22,30,'epidermis','t'],[38,60,'glandula sudorifera – znojnica','o'],[22,48,'dermis','t'],[22,70,'tela subcutanea','t'],
 [47,45,'glandula sebacea – lojnica','o'],[58,37,'čutni živčni končič','z'],[44,55,'m. arrector pili','m'],[56,71,'arteriola','z'],[61,49,'živec','z']])
f('1-6',3,cap='Plasti povrhnjice (od zgoraj navzdol): stratum corneum, granulosum, spinosum, basale. V trnasti plasti Langerhansova celica (imunska), v bazalni melanocit.',a=[
 [40,4,'stratum corneum – rožena plast','t'],[30,12,'stratum granulosum – zrnata plast','t'],[66,30,'stratum spinosum – trnasta plast','t'],
 [46,40,'Langerhansova celica (imunska obramba)','t'],[22,70,'stratum basale – bazalna plast','t'],[28,79,'delitev celice (mitoza)','t'],[63,71,'melanocit','t'],[60,88,'dermis – kapilara','z']])
f('1-6',4,cap='Melanociti v bazalni plasti z izrastki oddajajo melanosome (pigment) keratinocitom; zgoraj rožena plast.',a=[
 [40,22,'stratum corneum – rožena plast','t'],[45,35,'keratinociti','t'],[57,62,'melanosomi (pigment)','t'],[51,77,'melanocit','t'],[33,74,'stratum basale – bazalna plast','t'],[25,85,'dermis','t']])
f('1-6',5,cap='Merklova celica (tipalni disk) – mehanoreceptor ob bazalni plasti povrhnjice, povezan z živčnim končičem; zaznava rahel dotik.',a=[
 [21,23,'lega Merklove celice (povečano desno)','o'],[79,45,'Merklova celica','t'],[88,63,'živčni končič – dotik','z'],[19,40,'dlaka (pilus)','o']])
f('1-6',6,cap='Plasti kože: epidermis, dermis, hypodermis (podkožje z maščevjem in večjimi žilami).',a=[
 [36,40,'pilus – dlaka','o'],[70,36,'epidermis – povrhnjica','t'],[71,55,'dermis – usnjica','t'],[25,70,'glandula sudorifera – znojnica','o'],
 [40,81,'arterija in vena','z'],[30,90,'hypodermis – maščobno tkivo','t']])
f('2-1',2,cap='Lobanjsko dno od spodaj (norma basilaris): trdo nebo, choanae, foramen magnum s kondili, processus styloideus in mastoideus.',a=[
 [44,6,'arcus alveolaris – zobni lok','k'],[54,14,'processus palatinus maxillae','k'],[54,27,'os palatinum – nebnica','k'],[51,36,'vomer – ralo','k'],
 [57,42,'processus pterygoideus (lamina lateralis)','k'],[33,49,'fossa mandibularis','s'],[41,56,'condylus occipitalis','s'],[50,63,'foramen magnum','k'],
 [63,54,'processus styloideus','k'],[70,60,'processus mastoideus','k'],[50,82,'os occipitale – zatilnica','k'],[50,47,'pars basilaris ossis occipitalis','k']])
f('2-1',3,cap='Levo: m. temporalis in m. masseter na lobanji. Sredina: čeljustni sklep z vezmi. Desno: deli mandibule.',a=[
 [32,25,'m. temporalis','m'],[22,56,'m. masseter','m'],[48,52,'arcus zygomaticus','k'],[49,80,'ramus mandibulae','k'],[42,68,'lig. laterale (TMJ)','s'],
 [89.5,65,'processus coronoideus','k'],[91,68,'incisura mandibulae','k'],[95.5,63,'caput mandibulae','s'],[93.5,69,'collum mandibulae','k'],
 [86,75,'ramus mandibulae','k'],[88,83,'angulus mandibulae','k'],[76.5,83,'foramen mentale','k'],[80,86,'corpus mandibulae','k']])
f('2-1',4,cap='Čeljustni sklep (articulatio temporomandibularis), sagitalni prerez: caput mandibulae v fossa mandibularis, med njima discus articularis, ki sklep razdeli na zgornji in spodnji del.',a=[
 [35,30,'squama temporalis','k'],[40,41,'discus articularis','s'],[48,40,'tuberculum articulare','s'],[27,45,'capsula articularis','s'],
 [42,52,'caput mandibulae','s'],[40,73,'lig. stylomandibulare','s'],[58,45,'m. pterygoideus lateralis','m'],[68,65,'m. pterygoideus medialis','m']])
f('2-1',1,cap='Kosti lobanje od strani (norma lateralis). Možganska lobanja: čelnica, temenica, senčnica, zatilnica, zagozdnica, rešetnica. Obrazna: nosnica, solznica, ličnica, maxilla, mandibula.',a=FIX['1-2'][5]['a'])
f('2-2',1,cap='Hrbtenica od strani: krivine (vratna lordoza, prsna kifoza, ledvena lordoza, sakralna kifoza); lig. nuchae in lig. supraspinale.',a=[
 [57,19,'protuberantia occipitalis externa','k'],[60,27,'ligamentum nuchae','s'],[59,35,'processus spinosus C7 (vertebra prominens)','k'],[64,29,'lordosis cervicalis – vratna lordoza','k'],
 [62,50,'kyphosis thoracica – prsna kifoza','k'],[57,62,'lig. supraspinale','s'],[66,74,'lordosis lumbalis – ledvena lordoza','k'],[61,88,'os sacrum','k'],[58,95,'os coccygis – trtica','k']])
f('2-2',2,cap='Vratno vretence s ploščico in živcem: medvretenčna ploščica (nucleus pulposus + anulus fibrosus), spinalni živec, foramen transversarium (skozi gre a. vertebralis).',a=[
 [50,10,'medulla spinalis – hrbtenjača','z'],[47,24,'n. spinalis – hrbtenjačni živec','z'],[67,24,'nucleus pulposus','s'],[76,28,'anulus fibrosus','s'],
 [38,56,'processus articularis superior','k'],[25,65,'processus spinosus','k'],[44,77,'tuberculum posterius','k'],[56,77,'foramen transversarium','k'],
 [61,78,'tuberculum anterius','k'],[75,72,'corpus vertebrae','k']])
f('2-2',3,cap='Zgornja vratna sklepa od zadaj (odstranjen lok): dens axis drži lig. apicis dentis in ligg. alaria; art. atlantooccipitalis.',a=[
 [52,8,'clivus','k'],[62,13,'os occipitale','k'],[52,35,'lig. apicis dentis','s'],[30,42,'art. atlantooccipitalis','s'],[57,45,'lig. alare','s'],
 [52,52,'dens axis','k'],[61,60,'atlas (C1)','k'],[70,81,'axis (C2)','k']])
f('2-2',4,cap='Zgoraj: prsni vretenci T4–T5 s sklepnimi jamicami za rebro. Spodaj: rebro se z vretencem stika dvakrat – glavica s telesom (foveae costales), tuberculum s prečnim odrastkom.',a=[
 [49,10,'corpus vertebrae T4','k'],[43,12,'fovea costalis inferior (T4)','s'],[45,15,'fovea costalis superior (T5)','s'],[38,17,'fovea costalis processus transversi','s'],
 [37,26,'processus spinosus – dolg, strm','k'],[55,33,'costa V – 5. rebro','k'],[75,35,'cartilago costalis','k'],
 [47,66,'processus spinosus','k'],[36,72,'fovea costalis processus transversi','s'],[61,73,'tuberculum costae','s'],[60,80,'collum costae','k'],
 [53,87,'caput costae','s'],[41,85,'fovea costalis superior','s'],[43,92,'corpus vertebrae','k']])
f('2-2',5,cap='Prsni koš od spredaj s trebušno prepono: desna kupola stoji višje (pod njo jetra), kraka prepone se pripenjata na ledvena vretenca.',a=[
 [50,25,'sternum – prsnica','k'],[30,22,'costa – rebro','k'],[43,25,'cartilago costalis – rebrni hrustanec','k'],[27,60,'diaphragma – desna kupola','m'],
 [77,58,'diaphragma – leva kupola','m'],[49,82,'crus dextrum – desni krak','m'],[57,75,'crus sinistrum – levi krak','m']])
f('2-3',1,cap='Lopatica od spredaj (facies costalis) in proksimalni del nadlahtnice od spredaj in od zadaj.',a=[
 [49,5,'acromion','k'],[44,12,'processus coracoideus','k'],[44,21,'cavitas glenoidalis','s'],[28,45,'fossa subscapularis','k'],
 [32,71,'caput humeri','s'],[27,72,'tuberculum majus','k'],[33,74,'collum anatomicum','k'],[32,77,'tuberculum minus','k'],[30,78,'sulcus intertubercularis','k'],
 [33,83,'collum chirurgicum – pogosto mesto zloma','k'],[29,88,'crista tuberculi majoris','k'],[70,73,'tuberculum majus (pogled od zadaj)','k'],[62,77,'collum anatomicum','k']])
f('2-3',2,cap='M. supraspinatus – origo fossa supraspinata, insertio zgornja ploskev tuberculum majus; začne abdukcijo nadlakti (prvih ~15°).',a=[
 [35,15,'m. supraspinatus (pogled od zadaj)','m'],[50,45,'clavicula','k'],[58,52,'acromion','k'],[50,59,'m. supraspinatus','m'],[43,64,'fossa supraspinata – origo','k'],
 [62,62,'tuberculum majus – insertio','k'],[48,67,'spina scapulae','k'],[45,80,'fossa infraspinata','k']])
f('2-3',3,cap='Komolčni sklep od spredaj: skupna sklepna ovojnica, kolateralni vezi, lig. anulare radii (objema glavico koželjnice), chorda obliqua in membrana interossea.',a=[
 [47,12,'humerus','k'],[63,30,'capsula articularis','s'],[33,40,'lig. collaterale radiale','s'],[68,45,'lig. collaterale ulnare','s'],[36,52,'lig. anulare radii','s'],
 [46,61,'lig. quadratum','s'],[45,67,'tendo m. bicipitis brachii (odrezana)','m'],[49,71,'chorda obliqua','s'],[39,90,'radius – koželjnica','k'],[52,90,'ulna – podlahtnica','k']])
f('2-3',4,cap='Zgoraj: art. radiocarpea (med radiusom in proksimalno vrsto) in art. mediocarpea (med obema vrstama). Spodaj: 8 zapestnic – proksimalna vrsta (scaphoideum, lunatum, triquetrum, pisiforme), distalna (trapezium, trapezoideum, capitatum, hamatum).',a=[
 [30,30,'art. radiocarpea','s'],[70,20,'art. mediocarpea','s'],[55,55,'ossa metacarpalia I–V','k'],[61,62,'os trapezoideum','k'],[63,67,'os trapezium','k'],
 [56,69,'os capitatum','k'],[52,69,'os hamatum','k'],[49,72,'os pisiforme','k'],[51,76,'os triquetrum','k'],[54,78,'os lunatum','k'],[59,74,'os scaphoideum','k'],
 [62,85,'processus styloideus radii','k'],[47,88,'processus styloideus ulnae','k'],[60,92,'radius','k'],[49,92,'ulna','k']])
f('2-3',5,cap='Kosti roke: ossa carpi (8), ossa metacarpalia (5), phalanges (14 – palec ima samo dve). Zeleno: zgoraj CMC sklepi, spodaj MCP sklepi.',a=[
 [42,6,'ossa carpi – zapestnice','k'],[36,10,'art. carpometacarpea (CMC)','s'],[61,58,'os metacarpale III','k'],[55,69,'art. metacarpophalangea (MCP)','s'],
 [55,76,'phalanx proximalis','k'],[55,82,'art. interphalangea proximalis (PIP)','s'],[55,86,'phalanx media','k'],[54,90,'art. interphalangea distalis (DIP)','s'],
 [62,96,'phalanx distalis','k'],[49,61,'MCP palca','s']])
f('2-3',6,cap='Medenica od spredaj: os coxae (ilium, ischium, pubis) + os sacrum + os coccygis. Art. sacroiliaca povezuje križnico in črevnico.',a=[
 [18,32,'os ilium – črevnica','k'],[30,25,'art. sacroiliaca','s'],[52,40,'os sacrum – križnica','k'],[50,59,'os coccygis – trtica','k'],
 [27,50,'linea terminalis – meja male medenice','k'],[50,75,'symphysis pubica','s'],[52,83,'arcus pubicus – sramni lok','k']])
f('2-3',7,cap='Medenica od spredaj (fotografija): symphysis pubica (modro) – hrustančni sklep (fibrokartilaginozni disk) med sramnicama.',a=[
 [20,25,'ala ossis ilii – krilo črevnice','k'],[50,45,'os sacrum – foramina sacralia anteriora','k'],[80,58,'acetabulum – ponvica kolka','s'],[58,63,'ramus superior ossis pubis','k'],
 [50,70,'symphysis pubica','s'],[37,70,'foramen obturatum','k'],[32,90,'os ischii – sednica','k']])
f('2-3',8,cap='Kolčni sklep od spredaj: lig. iliofemorale (najmočnejša vez telesa, preprečuje hiperekstenzijo), lig. pubofemorale, membrana obturatoria.',a=[
 [48,10,'os ilium','k'],[48,40,'labrum acetabuli (cotyloid ligament)','s'],[49,46,'caput femoris','s'],[30,52,'trochanter major','k'],
 [42,55,'lig. iliofemorale','s'],[61,55,'lig. pubofemorale','s'],[82,52,'os pubis','k'],[76,63,'membrana obturatoria','s'],[70,70,'os ischii','k'],
 [36,85,'femur','k'],[46,86,'trochanter minor','k']])
f('2-3',9,cap='Sindezmozi: membrana interossea med radiusom in ulno (podlaket) ter med tibio in fibulo (golen) – vlaknati sklep, prenaša sile med kostema.',a=[
 [34,55,'membrana interossea antebrachii','s'],[39,68,'ulna','k'],[30,76,'radius','k'],[59,30,'fibula – mečnica','k'],[68,30,'tibia – golenica','k'],[62,46,'membrana interossea cruris','s']])
f('2-3',10,cap='a – gleženj od zadaj: vilice iz obeh maleolov objemajo talus (zgornji skočni sklep). b – stopalo z medialne strani: sustentaculum tali, vezi podplata.',a=[
 [39,8,'fibula','k'],[52,8,'tibia','k'],[37,25,'malleolus lateralis','k'],[63,22,'malleolus medialis','k'],[54,32,'talus – skočnica','k'],
 [41,38,'calcaneus – petnica','k'],[57,40,'os naviculare','k'],[51,56,'malleolus medialis','k'],[55,63,'talus','k'],[44,70,'os naviculare','k'],
 [35,74,'os cuneiforme mediale','k'],[49,70,'lig. talocalcaneum interosseum','s'],[51,76,'sustentaculum tali','k'],[48,80,'lig. calcaneonaviculare plantare (»spring«)','s'],
 [62,83,'calcaneus','k'],[42,90,'aponeurosis plantaris','s']])
f('3-1',1,cap='Hialina hrustančevina (HE, veliko povečanje): hondrociti v lakunah, pogosto po 2–4 skupaj v izogenih skupinah (nastanejo z delitvijo ene celice); okoli njih bazofilni teritorialni matriks.',a=[
 [48,54,'hondrocit v lakuni','t'],[45,62,'izogena skupina (4 celice)','t'],[31,48,'izogena skupina (2 celici)','t'],[56,40,'teritorialni matriks – temnejši obroč','t'],[45,30,'interteritorialni matriks – svetel','t']])
f('3-1',2,cap='Kje je hrustanec v telesu. Modro hialini (nos, grlo, sapnik, rebra, sklepne ploskve), zeleno elastični (uhelj, epiglotis), rdeče vezivni (medvretenčne ploščice, simfiza, meniskus).',a=[
 [33,12,'uhelj – elastični','t'],[40,13,'nos – hialini','t'],[44,23,'sklepni hrustanec – hialini','t'],[39,32,'rebrni hrustanec – hialini','t'],
 [37,35,'medvretenčna ploščica – vezivni','t'],[34,55,'symphysis pubica – vezivni','t'],[33,78,'meniscus – vezivni','t'],[34,79,'sklepni hrustanec kolena – hialini','t'],
 [77,4,'epiglottis – elastični','t'],[75,8,'cartilago thyroidea – hialini','t'],[77,13,'cartilago cricoidea – hialini','t'],[79,19,'trachea – hialini obročki','t']])
f('3-1',3,cap='Hialina hrustančevina pod perihondrijem: hondrociti ležijo v lakunah, obdani z amorfnim matriksom (kolagen tipa II).',a=[
 [70,20,'perichondrium – perihondrij','t'],[44,38,'hondrocit','t'],[56,37,'lacuna – lakuna','t'],[37,68,'matriks – medceličnina','t'],[66,67,'lakuna z hondrocitom','t']])
f('3-1',4,crop=[0,0,76,100],cap='Hialina hrustančevina – rast: perihondrij (vezivna ovojnica) → hondroblasti (mladi, sploščeni) → hondrociti v izogenih skupinah globlje.',a=[
 [30,20,'perichondrium – perihondrij','t'],[38,37,'chondroblasti – hondroblasti (mladi, sploščeni)','t'],[46,70,'izogena skupina hondrocitov','t'],[28,63,'izogena skupina – hondrociti v lakunah','t']])
f('3-1',5,cap='Elastična hrustančevina (uhelj, epiglotis): gosta temna mreža elastičnih vlaken okoli lakun s hondrociti; zgoraj perihondrij.',a=[
 [50,6,'perichondrium – perihondrij','t'],[45,31,'hondrocit v lakuni','t'],[56,52,'elastična vlakna – temna mreža','t']])
f('3-1',6,cap='Vezivna hrustančevina (medvretenčna ploščica, simfiza, meniski): debeli snopi kolagenskih vlaken tipa I, med njimi hondrociti v vrstah; ni perihondrija.',a=[
 [60,30,'kolagenska vlakna tipa I – snopi','t'],[40,49,'hondrociti v vrstah','t'],[83,83,'hondrocit v lakuni','t']])
f('3-2',1,cap='Pravi (sinovijski) sklep – shema in koleno v prerezu. Sklepna ovojnica = zunanja fibrozna plast + notranja sinovijska membrana; sklepni hrustanec je hialin.',a=[
 [30,14,'periosteum – pokostnica','k'],[29,28,'ligamentum – vez','s'],[25,48,'membrana fibrosa – fibrozna ovojnica','s'],[38,45,'cavitas articularis','s'],
 [30,60,'membrana synovialis','s'],[41,50,'cartilago articularis – hialini hrustanec','s'],[33,75,'substantia compacta – kompaktna kost','k'],
 [74,15,'femur','k'],[71,34,'membrana synovialis (koleno)','s'],[68,58,'corpus adiposum infrapatellare','o'],[80,57,'meniscus','s'],[75,77,'tibia','k']])
f('3-2',2,cap='Sinovijski sklep: kosti s hialinim sklepnim hrustancem, sklepna votlina s sinovijsko tekočino, sklepna ovojnica (zunaj fibrozna, znotraj sinovijska membrana).',a=[
 [46,22,'kost – epifiza','k'],[45,51,'cartilago articularis','s'],[58,45,'membrana synovialis','s'],[60,58,'capsula articularis','s'],
 [50,58,'cavitas articularis – sinovijska tekočina','s'],[46,80,'kost','k']])
f('3-2',4,cap='Fibrozni (vezivni) sklepi: sutura – lobanjski šiv (med kostmi le malo veziva, skoraj negiben); syndesmosis – membrana interossea med radiusom in ulno.',a=[
 [46,10,'sutura – lobanjski šiv','s'],[34,20,'diploë – gobasta kostnina','k'],[46,16,'lamina externa – kompaktna kost','k'],[24,51,'sutura coronalis','s'],
 [79,40,'ulna','k'],[77,48,'radius','k'],[81,62,'membrana interossea – syndesmosis','s']])
f('3-2',5,cap='Hrustančni sklepi: primarni (synchondrosis – epifizna ploščica iz hialinega hrustanca, z rastjo zakosteni) in sekundarni (symphysis – vezivni hrustanec, npr. medvretenčna ploščica).',a=[
 [30,28,'cartilago articularis','s'],[26,30,'caput femoris','k'],[25,40,'epifizna ploščica – synchondrosis','s'],[16,60,'femur','k'],
 [71,16,'discus intervertebralis – symphysis','s'],[71,55,'corpus vertebrae','k']])
f('3-2',6,cap='Tipi sinovijskih sklepov v telesu: ravni (AC), tečajasti (komolec), vrtljivi (atlantoaksialni), sedlasti (CMC palca), jajčasti (MCP), kroglasti (kolk).',a=[
 [66,11,'art. acromioclavicularis – ravni sklep','s'],[62,34,'art. cubiti – tečajasti sklep','s'],[22,42,'art. atlantoaxialis mediana – vrtljivi (čepasti)','s'],
 [61,49,'art. carpometacarpea pollicis – sedlasti','s'],[57,68,'art. metacarpophalangea – jajčasti','s'],[34,70,'art. coxae – kroglasti sklep','s']])
f('3-3',4,cap='Sinovijski sklepi po obliki sklepnih ploskev in številu osi: 1 kroglasti (3 osi – rama, kolk), 2 jajčasti (2 osi – zapestje, MCP), 3 sedlasti (2 osi – CMC palca), 4 tečajasti (1 os – komolec, IP), 5 vrtljivi/čepasti (1 os – rotacija: atlantoaksialni, radioulnarni).',a=[
 [17,23,'1 · art. spheroidea – kroglasti, 3 osi','s'],[47,23,'2 · art. ellipsoidea – jajčasti, 2 osi','s'],[78,24,'3 · art. sellaris – sedlasti, 2 osi','s'],
 [25,72,'4 · ginglymus – tečajasti, 1 os','s'],[68,80,'5 · art. trochoidea – vrtljivi, 1 os','s']])
f('3-3',1,crop=[14,58,44,100],cap='Ramenski sklep – primer kroglastega sklepa: caput humeri v plitvi cavitas glenoidalis, ovojnica s sinovijsko membrano.',a=[
 [26,73,'capsula articularis – fibrozna','s'],[26,75,'membrana synovialis','s'],[27,77,'cavitas articularis – sinovijska tekočina','s'],
 [27,82,'caput humeri','k'],[37,82,'scapula – cavitas glenoidalis','k'],[33,80,'cartilago articularis','s'],[33,71,'clavicula','k']])
f('3-3',2,crop=[40,60,90,100],cap='Zgornja vratna sklepa (pogled od zadaj): A art. atlantooccipitalis – jajčasti (kimanje »da«), B art. atlantoaxialis – vrtljivi (obračanje »ne«).',a=[
 [67,71,'A · art. atlantooccipitalis – jajčasti','s'],[66,80,'B · art. atlantoaxialis lateralis','s'],[75,62,'os occipitale','k'],[75,74,'atlas (C1)','k'],[75,83,'axis (C2)','k']])
f('3-3',3,crop=[18,63,85,98],cap='Levo koleno z medialne strani: art. femoropatellaris in art. femorotibialis (tečajast sklep z možno rotacijo). Desno: radioulnarna sklepa (vrtljiva) in membrana interossea.',a=[
 [28,73,'art. femoropatellaris','s'],[36,78,'art. femorotibialis','s'],[23,81,'patella','k'],[30,88,'tibia','k'],
 [65,67,'art. radioulnaris proximalis','s'],[65,68,'lig. anulare radii','s'],[68,81,'membrana interossea antebrachii','s'],[66,91,'art. radioulnaris distalis','s']])
f('3-4',1,cap='Čeljustni sklep (articulatio temporomandibularis) – ponovitev s slike 2: discus articularis deli sklep na zgornji (drsenje naprej) in spodnji (vrtenje) del.',a=FIX['2-1'][4]['a'])
f('3-4',2,cap='Vezi zgornjih vratnih sklepov od zadaj (odstranjen lok): lig. cruciforme atlantis (= lig. transversum + longitudinalni snopi) drži dens ob atlasu; čez leži membrana tectoria.',a=[
 [52,15,'os occipitale – pars basilaris','k'],[35,44,'capsula art. atlantooccipitalis','s'],[60,40,'lig. alare','s'],[52,42,'lig. transversum atlantis','s'],
 [52,55,'lig. cruciforme atlantis','s'],[26,52,'atlas (C1)','k'],[59,58,'fasciculi longitudinales','s'],[63,64,'capsula art. atlantoaxialis lateralis','s'],[33,75,'axis (C2)','k']])
f('3-4',3,cap='Dens axis z vezmi od zadaj: lig. apicis dentis (od konice densa do foramen magnum) in ligg. alaria (od densa do kondilov zatilnice) – omejujeta rotacijo.',a=FIX['2-2'][3]['a'])
f('3-4',4,cap='Dolgi vezi hrbtenice: lig. longitudinale anterius po sprednji strani teles vretenc (preprečuje hiperekstenzijo), lig. longitudinale posterius v vretenčnem kanalu.',a=[
 [12,40,'lig. longitudinale anterius','s'],[21,32,'discus intervertebralis','s'],[83,30,'lig. longitudinale posterius','s'],[73,40,'discus intervertebralis','s'],[22,10,'corpus vertebrae','k']])
f('3-4',5,cap='Kratke vezi hrbtenice: ligamenta flava (med loki, elastične – rumene), lig. interspinale, lig. supraspinale, lig. intertransversarium; foramen intervertebrale.',a=[
 [13,27,'foramen intervertebrale','k'],[24,32,'discus intervertebralis','s'],[14,6,'lig. supraspinale','s'],[12,72,'ligamenta flava','s'],[35,77,'lig. flavum','s'],
 [79,32,'lig. longitudinale anterius','s'],[87,35,'lig. longitudinale posterius','s'],[81,46,'lig. flavum','s'],[77,53,'lig. intertransversarium','s'],
 [90,56,'lig. supraspinale','s'],[90,62,'lig. interspinale','s']])
f('3-4',6,cap='Sklepa rebra z vretencem: art. capitis costae (glavica rebra – foveae costales dveh vretenc) in art. costotransversaria (tuberculum costae – prečni odrastek).',a=FIX['2-2'][4]['a'])
f('3-5',1,cap='Art. sternoclavicularis (frontalni prerez levo): sklepni disk deli sklep na dva dela; ojačata ga lig. sternoclaviculare in lig. costoclaviculare. Edini pravi sklep med zgornjim udom in trupom.',a=[
 [24,15,'clavicula','k'],[41,26,'discus articularis','s'],[54,31,'lig. interclaviculare','s'],[22,40,'capsula articularis','s'],
 [22,30,'lig. costoclaviculare','s'],[22,51,'cartilago costalis I','k'],[45,55,'manubrium sterni','k'],[69,46,'lig. sternoclaviculare anterius','s'],
 [62,69,'lig. sternocostale radiatum','s'],[50,82,'synchondrosis sternalis','s']])
f('3-5',2,cap='Ramenski obroč od spredaj: art. acromioclavicularis povezuje lateralni konec ključnice z akromionom (zeleno = akromion).',a=[
 [44,10,'acromion','k'],[47,8,'art. acromioclavicularis','s'],[66,7,'clavicula','k'],[48,12,'processus coracoideus','k'],
 [40,22,'art. humeri – ramenski sklep','s'],[62,30,'scapula – facies costalis','k'],[36,55,'humerus','k']])
f('3-5',3,cap='Ramenski sklep (frontalni prerez): plitva cavitas glenoidalis, poglobljena z labrum glenoidale; nad sklepom akromion, lig. coracoacromiale in bursa subacromialis; skozi ovojnico poteka tetiva dolge glave bicepsa.',a=[
 [32,16,'clavicula','k'],[38,22,'tendo m. supraspinati','m'],[39,29,'labrum glenoidale','s'],[40,38,'cavitas glenoidalis','s'],[30,45,'scapula','k'],
 [41,57,'membrana synovialis','s'],[40,64,'membrana fibrosa','s'],[60,17,'acromion','k'],[42,20,'lig. acromioclaviculare','s'],[56,22,'lig. coracoacromiale','s'],
 [57,26,'bursa subacromialis','s'],[64,40,'capsula articularis','s'],[64,50,'tendo caput longum m. bicipitis','m'],[50,40,'caput humeri','k'],[40,50,'cartilago articularis','s'],[52,80,'humerus','k']])
f('3-5',4,cap='Komolčni sklep z medialne strani: zeleno = sklepna ovojnica (capsula articularis); pahljačasta lig. collaterale ulnare (trije snopi) stabilizira komolec proti valgusni sili.',a=[
 [21,30,'humerus','k'],[19,60,'capsula articularis (zeleno)','s'],[41,58,'lig. collaterale ulnare – sprednji snop','s'],[37,70,'lig. collaterale ulnare – zadnji/prečni snop','s'],
 [16,62,'olecranon ulnae','k'],[70,72,'ulna','k'],[70,58,'radius','k']])
f('3-5',5,cap='Radioulnarna sklepa in membrana interossea – ponovitev s slike 2: art. radioulnaris proximalis (lig. anulare objema glavico radiusa) in distalis delujeta skupaj pri pronaciji/supinaciji.',a=FIX['2-3'][3]['a'])
f('3-5',6,cap='Sklepi zapestja – ponovitev s slike 2: art. radiocarpea (jajčasti sklep) in art. mediocarpea; 8 zapestnic v dveh vrstah.',a=FIX['2-3'][4]['a'])
f('3-5',7,crop=[40,35,82,100],cap='Sklepi roke: CMC (sedlasti pri palcu), MCP (jajčasti), PIP in DIP (tečajasta). Zeleno = sklepne ovojnice MCP sklepov.',a=[
 [55,50,'art. carpometacarpea (CMC)','s'],[56,69,'art. metacarpophalangea (MCP)','s'],[55,81,'art. interphalangea proximalis (PIP)','s'],
 [55,89,'art. interphalangea distalis (DIP)','s'],[49,61,'MCP palca','s'],[47,66,'IP palca – samo en sklep','s']])
f('3-6',1,cap='Art. sacroiliaca – ponovitev s slike 2: zelo malo gibljiv sinovijski sklep med križnico in črevnico, ojačan z močnimi vezmi.',a=FIX['2-3'][6]['a'])
f('3-6',2,cap='Symphysis pubica – ponovitev s slike 2: sekundarni hrustančni sklep (vezivni hrustanec) med sramnicama.',a=FIX['2-3'][7]['a'])
f('3-6',3,cap='Art. coxae – ponovitev s slike 2: kroglasti sklep z globoko ponvico (labrum acetabuli); lig. iliofemorale, pubofemorale in ischiofemorale ovijajo ovojnico.',a=FIX['2-3'][8]['a'])
f('3-6',4,cap='Koleno: zgoraj od spredaj (zeleno = meniski), spodaj tibialni plato od zgoraj. Meniscus medialis je C-oblike in zraščen z lig. collaterale tibiale (zato pogosteje poškodovan); meniscus lateralis je bolj okrogel in gibljiv.',a=[
 [45,10,'femur','k'],[47,28,'menisci (zeleno)','s'],[48,42,'tibia','k'],[41,42,'fibula','k'],[57,66,'lig. patellae','s'],[52,68,'bursa infrapatellaris profunda','o'],
 [53,74,'lig. transversum genus','s'],[40,84,'meniscus medialis – C-oblike','s'],[54,81,'lig. cruciatum anterius (ACL)','s'],[52,92,'lig. cruciatum posterius (PCL)','s'],[66,81,'meniscus lateralis – O-oblike','s']])
f('3-6',5,crop=[50,38,100,100],cap='Koleno od spredaj in od strani: križni vezi (ACL od spredaj-zgoraj tibije navzgor-nazaj; PCL obratno) in kolateralni vezi (medialna – tibialis, lateralna – fibularis).',a=[
 [56,50,'tetiva m. quadriceps femoris in patella','m'],[70,63,'meniscus','s'],[72,55,'lig. cruciatum anterius / posterius','s'],[66,72,'lig. collaterale','s'],[83,70,'lig. patellae','s']])
f('3-6',8,cap='Gleženj z medialne strani: lig. deltoideum (mediale) – trikotna vez od notranjega maleola do talusa, navikulare in kalkaneusa; spodaj vezi podplata.',a=[
 [60,15,'tibia','k'],[56,48,'lig. deltoideum (lig. mediale)','s'],[35,56,'os naviculare','k'],[71,48,'lig. talotibiale posterius','s'],
 [75,58,'lig. talocalcaneum mediale','s'],[42,72,'lig. calcaneonaviculare plantare','s'],[57,80,'lig. plantare longum','s'],[78,82,'calcaneus','k'],[18,62,'capsula articularis','s']])
f('3-6',6,cap='Art. tibiofibularis in membrana interossea cruris – ponovitev s slike 2.',a=FIX['2-3'][9]['a'])
f('3-6',7,cap='Art. talocruralis (zgornji skočni sklep – tečajasti: dorzalna/plantarna fleksija) in art. subtalaris / talocalcaneonavicularis (spodnji skočni sklep – inverzija/everzija) – ponovitev s slike 2.',a=FIX['2-3'][10]['a'])
f('3-7',1,cap='Ovojnice skeletne mišice: epimizij ovija celo mišico, perimizij posamezne snope (fascikle), endomizij posamezna mišična vlakna. Ovojnice se na koncu zlijejo v kito.',a=[
 [40,31,'epimysium – ovija celo mišico','m'],[66,16,'perimysium – ovija snop','m'],[68,28,'krvna žila','z'],[72,36,'myocytus – mišično vlakno','m'],
 [62,43,'fasciculus – snop vlaken','m'],[62,57,'endomysium – ovija vlakno','m'],[16,70,'tendo – kita','s'],[18,90,'os – kost','k']])
f('3-7',2,cap='Deli mišice: caput (glava – na izvoru, origo), venter (trebuh), cauda (rep) in kita/aponevroza na narastišču (insertio); celo mišico ovija fascija.',a=[
 [50,24,'caput – glava (origo)','m'],[46,42,'fascia – ovojnica','m'],[53,52,'venter – trebuh','m'],[50,80,'cauda – rep','m'],[51,90,'tendo – kita (insertio)','s']])
f('3-7',3,cap='Večglave mišice: levo dvoglava (biceps), desno troglava (triceps) – več glav z različnimi izvori se združi v skupen trebuh in eno kito.',a=[
 [31,20,'caput 1','m'],[40,18,'caput 2','m'],[37,55,'skupni trebuh','m'],[36,85,'tendo – skupna kita','s'],
 [59,16,'caput 1','m'],[66,14,'caput 2','m'],[72,16,'caput 3','m'],[67,85,'tendo – skupna kita','s']])
f('3-7',4,cap='Skeletno mišično vlakno: več jeder na robu (pod sarkolemo), polno miofibril; vsaka miofibrila je niz sarkomer (pas I – svetel, pas A – temen, cona H, Z disk). Sarkoplazemski retikulum hrani Ca²⁺.',a=[
 [30,11,'nuclei – jedra ob robu vlakna','m'],[28,21,'pas I – svetel','m'],[38,33,'pas A – temen','m'],[58,12,'mitochondrion','t'],[64,20,'sarcolemma – celična membrana','m'],
 [70,25,'myofibrilla','m'],[22,72,'reticulum sarcoplasmicum (Ca²⁺)','m'],[30,72,'aktin – tanki filament','m'],[37,72,'Z disk (črta Z)','m'],
 [51,72,'cona H – samo miozin','m'],[52,63,'sarkomera (Z do Z)','m'],[78,69,'miozin – debeli filament','m'],[79,82,'črta M','m'],[37,89,'pas I','m'],[51,89,'pas A','m']])
f('3-7',5,cap='Sarkomera – osnovna krčljiva enota (od Z do Z). Pas I = samo aktin (seka ga Z), pas A = dolžina miozina, cona H = samo miozin (seka jo M). Pri krčenju se skrajšata pas I in cona H, pas A ostane enak.',a=[
 [40,9,'sarkomera = od Z do Z','m'],[28,30,'črta Z na mikrofotografiji','m'],[28,52,'Z disk','m'],[24,62,'tanki filament – aktin','m'],[49,65,'črta M','m'],
 [59,56,'debeli filament – miozin','m'],[49,84,'cona H – samo miozin','m'],[25,86,'pas I – samo aktin','m'],[50,90,'pas A – dolžina miozina','m']])
f('3-7',6,cap='Krčljivi aparat v nemišični celici (npr. miofibroblast): snopi aktinskih filamentov, ki jih miozin II vleče drug ob drugem; z integrini so pripeti na celično membrano.',a=[
 [32,68,'aktinski filamenti','m'],[46,57,'miozin II – povezuje filamente','m'],[60,58,'miozin II','m'],[50,83,'plasmalemma – celična membrana','t'],
 [22,85,'integrini – pritrdišče na membrano','t'],[22,81,'povezovalne beljakovine','t'],[50,27,'jedro celice (shema celice zgoraj)','t']])
f('3-7',7,cap='Teorija drsečih filamentov: v skrčenem stanju aktin zdrsne ob miozinu proti črti M – razdalja Z–Z (A–A) se skrajša, dolžina miozina (pas A, B–D) ostane enaka.',a=[
 [30,20,'aktin – tanki filament','m'],[58,28,'miozin – debeli filament','m'],[30,26,'miozinske glavice (prečni mostički)','m'],
 [10,22,'Z disk – sproščeno','m'],[17,68,'Z disk – skrčeno, bliže sredini','m'],[54,28,'črta M (D)','m'],[22,40,'B – rob miozina (ne premakne se)','m'],[43,40,'C – konec aktina','m']])
f('3-7',8,cap='Živčno-mišični stik (motorična ploščica): akson sprosti acetilholin iz veziklov v sinaptično režo; receptorji na nagubani membrani mišičnega vlakna sprožijo akcijski potencial.',a=[
 [59,6,'myelinum – mielinska ovojnica','z'],[51,14,'akson motoričnega nevrona','z'],[44,37,'vezikli z acetilholinom','z'],[61,42,'mitohondriji v končiču','t'],
 [31,49,'sinaptična reža','z'],[25,57,'motorična ploščica','z'],[68,54,'receptorji za acetilholin','z'],[76,58,'mitohondrij mišičnega vlakna','t'],[35,74,'skeletno mišično vlakno','m']])
f('3-7',9,cap='Srčna mišičnina (HE): razvejane celice z enim centralnim jedrom; v krogu zeleno označene interkalarne ploščice (disci intercalares) – stiki med celicami s presledkovnimi stiki za prenos vzburjenja.',a=[
 [54,50,'discus intercalaris – interkalarna ploščica','m'],[50,56,'discus intercalaris','m'],[27,43,'jedro kardiomiocita – centralno','m'],[66,82,'razvejana vlakna','m']])
f('3-7',10,cap='Gladka mišičnina (HE): vretenaste celice z enim podolgovatim jedrom v sredini; brez prečne progavosti.',a=[
 [40,40,'vretenaste gladke mišične celice','m'],[34,22,'podolgovato jedro v sredini celice','m']])
f('3-7',11,cap='Od mišice do sarkomere: mišica → snop (fascikel) → mišično vlakno (celica) → miofibrila → sarkomera (aktin + miozin). Spodaj sarkomera s pasovi.',a=[
 [18,18,'tendo – kita','s'],[38,16,'musculus – mišica','m'],[42,21,'arterija, vena in živec','z'],[65,22,'fasciculus – snop','m'],[75,30,'myocytus – mišično vlakno','m'],
 [83,36,'myofibrilla','m'],[45,70,'črta Z','m'],[63,72,'črta M','m'],[48,79,'pas I','m'],[63,78,'cona H','m'],[63,80,'pas A','m'],[78,79,'aktin – tanki filament','m'],[74,80,'miozin – debeli filament','m']])
f('3-7',12,cap='Delitev po medsebojnem odnosu pri fleksiji komolca: m. biceps brachii je agonist (glavni izvajalec), m. brachialis in m. brachioradialis sta sinergista; m. triceps brachii bi bil antagonist.',a=[
 [43,25,'m. biceps brachii – agonist','m'],[34,50,'m. brachioradialis – sinergist','m'],[87,50,'m. biceps brachii (prerezan)','m'],[85,66,'m. brachialis – sinergist','m'],[75,78,'m. brachioradialis','m']])
f('3-7',13,cap='Mišica premika kost čez sklep: kita na izvoru (origo) in na narastišču (insertio), med njima mišični trebuh; sklep ima ovojnico z vezmi in hialin sklepni hrustanec.',a=[
 [38,59,'tendo – kita na izvoru (origo)','s'],[49,53,'venter – trebuh mišice','m'],[63,45,'tendo – kita na narastišču (insertio)','s'],[61,55,'os – kost','k'],
 [51,70,'capsula articularis in ligamenta','s'],[60,72,'cartilago articularis','s']])
f('3-8',1,cap='Narastišča mišic glave na lobanji (rdeče = izvori, modro = narastišča). Mimične mišice oživčuje n. facialis (VII), žvekalne n. trigeminus (V3), SCM in trapezius n. accessorius (XI).',a=[
 [55,30,'m. temporalis – origo (fossa temporalis)','m'],[44,62,'m. masseter – insertio (ramus mandibulae)','m'],[29,49,'m. zygomaticus – origo','m'],
 [27,42,'m. orbicularis oculi – origo','m'],[34,67,'m. buccinator – origo','m'],[27,72,'m. mentalis – origo','m'],
 [77,44,'m. sternocleidomastoideus – insertio','m'],[74,52,'m. semispinalis capitis – insertio','m'],[65,58,'m. splenius capitis – insertio','m']])
f('3-8',3,cap='Žvekalni mišici m. temporalis (origo fossa temporalis → insertio processus coronoideus) in m. masseter (arcus zygomaticus → angulus mandibulae); obe zapirata usta. Desno deli mandibule.',a=[
 [30,27,'m. temporalis – dvig in retrakcija mandibule','m'],[28,51,'art. temporomandibularis','s'],[18,70,'m. masseter – dvig mandibule','m'],
 [58,72,'fossa temporalis – origo m. temporalis','k'],[74,68,'processus condylaris','k'],[79,62,'incisura mandibulae','k'],[80,64,'processus coronoideus – insertio m. temporalis','k'],
 [77,81,'ramus mandibulae','k'],[78,90,'angulus mandibulae','k'],[86,85,'corpus mandibulae','k']])
f('3-8',4,cap='M. masseter (puščica) in kostne točke: arcus zygomaticus (origo), ramus in angulus mandibulae (insertio); na fotografiji desno deli mandibule.',a=[
 [32,25,'m. temporalis','m'],[22,57,'m. masseter','m'],[49,55,'arcus zygomaticus – origo m. masseter','k'],[48,78,'ramus mandibulae','k'],
 [91,63,'processus coronoideus','k'],[95,62,'caput mandibulae','s'],[92,72,'collum mandibulae','k'],[76,72,'corpus mandibulae','k'],[87,80,'angulus mandibulae','k'],[77,82,'foramen mentale','k']])
FIX['3-8'][4]['a']=[[32,25,'m. temporalis','m'],[22,57,'m. masseter','m'],[49,55,'arcus zygomaticus – origo m. masseter','k'],[48,78,'ramus mandibulae','k'],
 [88.5,64,'processus coronoideus','k'],[91,67,'incisura mandibulae','k'],[95.5,62,'caput mandibulae','s'],[93.5,65,'fovea pterygoidea','k'],[93.5,69,'collum mandibulae','k'],
 [86,75,'ramus mandibulae','k'],[88,83,'angulus mandibulae','k'],[80,80,'corpus mandibulae','k'],[76.5,83,'foramen mentale','k']]
f('3-8',5,cap='M. pterygoideus lateralis (zeleno): od lamina lateralis processus pterygoidei → fovea pterygoidea in sklepni disk; odpira usta, pomika mandibulo naprej. Levo spodaj kostne točke mandibule.',a=[
 [44,17,'m. pterygoideus lateralis','m'],[42,26,'m. pterygoideus medialis','m'],[29,58,'processus coronoideus','k'],[41,59,'fovea pterygoidea – insertio m. pteryg. lat.','k'],
 [44,57,'caput mandibulae','s'],[40,64,'collum mandibulae','k'],[63,62,'m. pterygoideus lateralis (zeleno)','m'],[61,74,'m. pterygoideus medialis','m']])
f('3-8',6,cap='M. pterygoideus medialis: od fossa pterygoidea → notranja stran angulus mandibulae (tuberositas pterygoidea); skupaj z m. masseter tvori »zanko« okoli angulusa in dviga mandibulo.',a=[
 [52,19,'m. pterygoideus lateralis','m'],[51,28,'m. pterygoideus medialis','m'],[62,61,'m. pterygoideus lateralis (zeleno)','m'],[60,75,'m. pterygoideus medialis','m'],
 [33,80,'angulus mandibulae','k'],[55,75,'m. masseter (zunaj)','m']])
f('3-8',7,cap='Mimične mišice (n. facialis): okrog očesa, nosu in ust; večinoma izvirajo na kosti in se naraščajo v kožo.',a=[
 [35,24,'m. frontalis – dvig obrvi, gube na čelu','m'],[29,31,'m. temporalis (žvekalna)','m'],[32,41,'m. orbicularis oculi – zapiranje očesa','m'],
 [38,46,'m. levator labii superioris','m'],[33,49,'m. zygomaticus major / minor – nasmeh','m'],[31,54,'m. masseter (žvekalna)','m'],[34,57,'m. buccinator','m'],[34,61,'m. risorius','m'],
 [44,37,'m. procerus','m'],[48,35,'m. corrugator supercilii – mrščenje','m'],[46,45,'m. nasalis','m'],[47,54,'m. orbicularis oris – zapiranje ust','m'],
 [52,61,'m. depressor anguli oris','m'],[54,62,'platysma','m'],[48,63,'m. depressor labii inferioris','m']])
f('3-8',8,crop=[0,0,25,82],cap='M. buccinator (lična mišica): od raphe pterygomandibularis do ustnega kota; stiska lice ob zobe (pihanje, žvečenje), pod njim parotidni izvod.',a=[
 [12,42,'m. buccinator','m'],[16,62,'raphe pterygomandibularis','s'],[19,71,'m. constrictor pharyngis superior','m'],[14,8,'ductus parotideus (prerezan)','o']])
f('3-8',9,cap='Sprednje vratne mišice: suprahioidne (nad os hyoideum), infrahioidne (pod njo – »trakaste«), m. sternocleidomastoideus, mm. scaleni; spodaj ključnica in manubrium.',a=[
 [45,21,'m. stylohyoideus','m'],[48,24.5,'m. digastricus – venter posterior','m'],[50,27,'v. jugularis interna','z'],[31,29,'a. carotis externa','z'],
 [35,31,'os hyoideum','k'],[46,33.5,'m. thyrohyoideus','m'],[45,38,'m. omohyoideus – venter superior','m'],[40,40,'cartilago thyroidea','o'],
 [42,41,'m. sternothyroideus','m'],[37,45,'m. sternohyoideus','m'],[26,52,'mm. scaleni','m'],[29,57,'m. sternocleidomastoideus','m'],
 [56,58,'m. omohyoideus – venter inferior','m'],[61,57,'m. trapezius','m'],[21,62,'clavicula','k'],[41,70,'manubrium sterni','k'],[73,62,'m. deltoideus','m']])
f('3-8',10,cap='Vrat od strani: globlje m. splenius cervicis, m. levator scapulae in mm. scaleni (ant., med., post.); med m. scalenus anterior in medius izstopa plexus brachialis. Spredaj SCM s sternalno in klavikularno glavo.',a=[
 [43,40,'m. splenius cervicis','m'],[44,52,'m. levator scapulae','m'],[49,64,'m. scalenus anterior','m'],[46,67,'m. scalenus medius','m'],[42,70,'m. scalenus posterior','m'],
 [28,75,'m. trapezius','m'],[62,42,'m. masseter','m'],[57,46,'m. digastricus – venter posterior','m'],[56,62,'m. sternocleidomastoideus','m'],
 [53,74,'SCM – caput sternale','m'],[50,76,'SCM – caput claviculare','m'],[43,84,'plexus brachialis','z'],[52,30,'a. carotis in v. jugularis','z']])
f('3-8',11,cap='Mimične mišice okrog nosu in ust (desno od spredaj) – kaj naredijo.',a=[
 [55.5,31.5,'m. corrugator supercilii – mršči obrvi','m'],[61,46,'m. levator labii sup. alaeque nasi – dvigne ustnico in nosnico','m'],
 [57,51,'m. levator labii superioris – dvigne zgornjo ustnico','m'],[57,65.5,'m. buccinator – stisne lice ob zobe','m'],
 [61,74,'m. depressor labii inferioris – spusti spodnjo ustnico','m'],[65,78,'m. mentalis – nabere kožo brade','m']])
f('4-1',1,cap='Predeli vratu od spredaj: regio cervicalis anterior (med obema SCM) s trikotniki, regio sternocleidomastoidea, regio cervicalis lateralis (med SCM in trapeziusom) s trigonum omoclaviculare.',a=[
 [49,10,'regio submentalis','o'],[38,22,'trigonum submandibulare','o'],[37,35,'trigonum caroticum','o'],[48,40,'regio laryngea – regio cervicalis anterior','o'],
 [61,48,'m. sternocleidomastoideus – regio sternocleidomastoidea','m'],[15,68,'m. trapezius','m'],[28,73,'m. omohyoideus – venter inferior','m'],
 [33,82,'trigonum omoclaviculare','o'],[76,70,'regio cervicalis lateralis','o'],[49,92,'incisura jugularis sterni','k']])
f('4-1',2,cap='Os hyoideum deli sprednje vratne mišice na suprahioidne (zgoraj, dno ustne votline) in infrahioidne (spodaj, »trakaste« mišice); ob strani v. jugularis interna.',a=[
 [54,14,'suprahioidne mišice','m'],[45,30,'os hyoideum – podjezičnica','k'],[32,50,'v. jugularis interna','z'],[45,42,'cartilago thyroidea','o'],
 [53,50,'infrahioidne mišice','m'],[45,57,'cartilago cricoidea','o'],[45,80,'trachea','o']])
f('4-1',3,cap='Suprahioidne mišice: m. digastricus (zeleno – dva trebuha, vmesna kita na os hyoideum), m. stylohyoideus (rumeno), m. mylohyoideus (rdeče – dno ustne votline).',a=[
 [46,22,'m. stylohyoideus','m'],[47,29,'m. digastricus – venter posterior','m'],[33,34,'m. mylohyoideus','m'],[28,39,'m. digastricus – venter anterior','m'],[49,57,'m. sternocleidomastoideus','m']])
f('4-1',4,cap='Infrahioidne (»trakaste«) mišice: m. sternohyoideus (zeleno), m. sternothyroideus (rumeno, globlje), m. thyrohyoideus (rdeče), m. omohyoideus (modro – dva trebuha, vmesna kita pod SCM).',a=[
 [39,37,'m. thyrohyoideus','m'],[46,33,'m. omohyoideus – venter superior','m'],[45,50,'m. sternohyoideus','m'],[38,63,'m. sternothyroideus','m'],[54,79,'m. omohyoideus – venter inferior','m'],[22,82,'clavicula','k']])
f('4-1',5,cap='M. sternocleidomastoideus deli vrat na sprednji trikotnik (trigonum colli anterius – zeleno) in stranski trikotnik (trigonum colli laterale – oranžno); spodnji trebuh m. omohyoideus odreže trigonum omoclaviculare.',a=[
 [43,36,'m. sternocleidomastoideus','m'],[57,38,'trigonum colli anterius','o'],[77,36,'mandibula','k'],[33,54,'trigonum colli laterale','o'],
 [30,68,'m. omohyoideus – venter inferior','m'],[22,79,'clavicula','k'],[35,74,'trigonum omoclaviculare (supraclaviculare)','o'],[62,46,'os hyoideum','k']])
f('4-1',6,cap='Prevertebralne mišice ležijo na sprednji strani vratnih vretenc: m. longus colli, m. longus capitis, m. rectus capitis anterior in lateralis – upogibajo glavo in vrat naprej.',a=[
 [49,15,'pars basilaris ossis occipitalis','k'],[52,22,'m. longus capitis (prerezan)','m'],[56,23,'condylus occipitalis','s'],[58,25,'m. rectus capitis anterior','m'],
 [63,24,'m. rectus capitis lateralis','m'],[64,30,'processus transversus atlantis','k'],[43,32,'m. longus capitis','m'],[44,52,'m. longus colli','m'],[36,40,'m. scalenus anterior','m']])
f('4-1',7,crop=[0,0,22,82],cap='Platysma – tanka podkožna mišica vratu (od fascije prsnega koša do spodnjega roba mandibule); napne kožo vratu, spusti ustni kot. Oživčuje jo n. facialis.',a=[
 [11,58,'platysma','m'],[7,35,'mimične mišice obraza','m']])
f('4-1',8,cap='M. sternocleidomastoideus (rdeče): origo – caput sternale (manubrium) in caput claviculare (medialna tretjina ključnice); insertio – processus mastoideus in linea nuchae superior. Enostransko: nagib na isto stran, rotacija obraza na nasprotno stran; obojestransko: ekstenzija glave, pomožna vdihalka.',a=[
 [58,17,'processus mastoideus – insertio','k'],[49,47,'m. sternocleidomastoideus','m'],[62,40,'m. splenius','m'],[58,55,'m. levator scapulae','m'],
 [53,70,'m. scalenus medius','m'],[51,70,'m. scalenus anterior','m'],[70,72,'m. trapezius','m'],[37,86,'caput sternale – origo','m'],[44,86,'caput claviculare – origo','m'],
 [32,40,'m. digastricus','m'],[30,60,'m. sternohyoideus','m'],[37,64,'m. omohyoideus','m']])
f('4-1',9,cap='Vratna fascija (fascia cervicalis): lamina superficialis (oranžno – ovija SCM in trapezius), lamina pretrachealis (zeleno – ovija infrahioidne mišice in organe), lamina prevertebralis (sivo – ovija globoke mišice); vagina carotica (modro) ovija žilno-živčni snop.',a=[
 [54,15,'mandibula','k'],[34,35,'lamina superficialis','o'],[45,54,'fascia visceralis (organska)','o'],[59,48,'vagina carotica','z'],
 [53,56,'lamina pretrachealis','o'],[67,66,'lamina prevertebralis','o'],[68,80,'clavicula','k']])
f('4-1',10,cap='Mm. scaleni: anterior in medius → 1. rebro, posterior → 2. rebro; dvigujejo rebra (pomožne vdihalke) in nagibajo vrat. Med anteriorjem in mediusom poteka plexus brachialis in a. subclavia.',a=[
 [15,52,'m. scalenus anterior','m'],[34,45,'m. scalenus medius','m'],[39,68,'m. scalenus posterior','m'],[8,82,'costa I – 1. rebro','k'],[42,81,'costa I','k'],
 [23,55,'m. longus colli','m'],[71,40,'mm. scaleni – stranski pogled (zeleno)','m']])
f('4-2',1,cap='Ligamentum nuchae – trikotna vezivna ploskev od protuberantia occipitalis externa do trna C7; spodaj se nadaljuje v lig. supraspinale. Izvor za m. trapezius in m. splenius.',a=[
 [57,19,'protuberantia occipitalis externa','k'],[59,27,'ligamentum nuchae','s'],[59,35,'processus spinosus C7 (vertebra prominens)','k'],[58,62,'lig. supraspinale','s']])
f('4-2',2,cap='M. trapezius: pars descendens (dvig lopatice), pars transversa (retrakcija), pars ascendens (spust lopatice); vsi trije skupaj rotirajo lopatico navzgor (abdukcija nad 90°). Oživčenje: n. accessorius (XI).',a=[
 [40,15,'m. trapezius','m'],[48,57,'lig. nuchae – origo','s'],[55,59,'pars descendens','m'],[59,67,'pars transversa','m'],[56,80,'pars ascendens','m'],
 [49,63,'processus spinosus C7','k'],[34,68,'acromion – insertio','k'],[33,71,'spina scapulae – insertio','k'],[37,64,'clavicula (lateralna tretjina) – insertio','k']])
f('4-2',3,cap='M. latissimus dorsi: origo – trni T7–L5 (prek fascia thoracolumbalis), crista iliaca, spodnja rebra, angulus inferior scapulae; insertio – crista tuberculi minoris (dno sulcus intertubercularis). Ekstenzija, addukcija, notranja rotacija nadlakti. Oživčenje: n. thoracodorsalis.',a=[
 [33,42,'origo – processus spinosi T7–L5','k'],[46,42,'angulus inferior scapulae – origo','k'],[44,56,'m. latissimus dorsi','m'],[38,72,'fascia thoracolumbalis – origo','s'],
 [46,76,'crista iliaca – origo','k'],[67,28,'insertio – crista tuberculi minoris','k']])
f('4-2',4,cap='Pritrdišča m. latissimus dorsi: crista iliaca (zeleno, origo), fascia thoracolumbalis prek trnov ledvenih vretenc (origo), sulcus intertubercularis humeri (rdeče, insertio).',a=[
 [12,8,'crista iliaca – origo','k'],[18,78,'processus spinosus ledvenega vretenca – origo prek fascije','k'],[57,42,'sulcus intertubercularis – insertio','k']])
f('4-2',5,cap='Površinski hrbet: m. trapezius zgoraj, m. latissimus dorsi spodaj; fascia thoracolumbalis v ledvenem predelu, fascia infraspinata nad m. infraspinatus.',a=[
 [38,30,'m. trapezius – kapucasta mišica','m'],[60,32,'fascia infraspinata','s'],[60,60,'m. latissimus dorsi – najširša hrbtna','m'],
 [46,82,'fascia thoracolumbalis','s'],[48,94,'crista iliaca','k'],[45,20,'m. trapezius – pars descendens','m']])
f('4-2',6,cap='M. levator scapulae (zeleno): origo – processus transversi C1–C4; insertio – angulus superior in margo medialis scapulae (nad spino). Dvigne lopatico in jo zavrti navzdol. Oživčenje: n. dorsalis scapulae.',a=[
 [24,10,'origo – processus transversi C1–C4','k'],[18,25,'m. levator scapulae','m'],[16,31,'angulus superior scapulae – insertio','k'],
 [62,66,'acromion','k'],[67,67,'processus coracoideus','k'],[72,64,'clavicula','k'],[59,69,'angulus acromialis','k'],[74,73,'spina scapulae','k'],[76,88,'scapula','k']])
f('4-2',7,cap='Zgoraj: mm. rhomboidei pod trapeziusom. Spodaj levo mm. rhomboidei (zeleno): minor C6–C7, major T1–T4 → margo medialis scapulae; retrakcija in dvig lopatice. Spodaj desno: m. serratus posterior superior.',a=[
 [17,20,'m. trapezius','m'],[25,14,'m. levator scapulae','m'],[25,21,'m. rhomboideus minor','m'],[27,30,'m. rhomboideus major','m'],[22,31,'vertebra C7','k'],
 [21,72,'mm. rhomboidei','m'],[16,80,'margo medialis scapulae – insertio','k'],[67,70,'m. serratus posterior superior','m']])
f('4-2',8,cap='M. serratus posterior superior: origo – trni C7–T3 (lig. nuchae); insertio – rebra 2–5; dvig reber (pomožna vdihalka).',a=[
 [44,58,'m. serratus posterior superior','m'],[50,51,'origo – procc. spinosi C7–T3','k'],[63,66,'insertio – rebra 2–5','k']])
f('4-2',9,cap='M. serratus posterior superior (zgoraj) in inferior (spodaj): inferior – origo trni T11–L2 (fascia thoracolumbalis), insertio rebra 9–12; spust reber.',a=[
 [44,30,'m. serratus posterior superior','m'],[40,74,'m. serratus posterior inferior','m'],[50,82,'origo – procc. spinosi T11–L2','k'],[63,68,'insertio – rebra 9–12','k']])
f('4-3',1,cap='M. splenius (zeleno zgoraj, rdeče spodaj): origo – lig. nuchae in trni C7–T6; m. splenius capitis → processus mastoideus in linea nuchae superior, m. splenius cervicis → processus transversi C1–C3. Ekstenzija in rotacija glave na isto stran.',a=[
 [45,10,'m. splenius capitis','m'],[56,24,'m. splenius cervicis','m'],[51,33,'origo – procc. spinosi C7–T6','k'],[47,84,'m. splenius – pogled od zadaj','m']])
f('4-3',2,cap='M. splenius od zadaj (rdeče) in od spredaj-zadaj (zeleno): splenius capitis zgoraj lateralno, splenius cervicis spodaj.',a=[
 [17,62,'m. splenius (obe porciji)','m'],[69,15,'m. splenius capitis','m'],[73,45,'origo – procc. spinosi','k']])
f('4-3',3,cap='Mm. erectores spinae – trije stebri od lateralno proti medialno: m. iliocostalis (I), m. longissimus (L), m. spinalis (S) – »I Love Spine«. Obojestransko ekstenzija hrbtenice, enostransko lateralna fleksija.',a=[
 [46,8,'processus mastoideus','k'],[47,15,'m. longissimus capitis','m'],[46,24,'m. iliocostalis cervicis','m'],[47,28,'m. longissimus cervicis','m'],
 [44,39,'m. iliocostalis thoracis','m'],[47,48,'m. longissimus thoracis','m'],[54,13,'m. spinalis capitis','m'],[54,20,'m. spinalis cervicis','m'],
 [51,51,'m. spinalis thoracis','m'],[45,75,'m. iliocostalis lumborum','m'],[47,88,'fascia thoracolumbalis','s']])
f('4-3',4,cap='M. iliocostalis (rdeče) – najbolj lateralni steber m. erector spinae: od crista iliaca in križnice na angulus costae vseh reber in na vratne prečne odrastke.',a=[
 [49,15,'m. multifidus','m'],[60,28,'m. iliocostalis cervicis – na zgornja rebra','m'],[61,50,'m. iliocostalis thoracis','m'],[61,74,'m. iliocostalis lumborum','m'],
 [55,40,'m. longissimus thoracis','m'],[52,30,'m. spinalis','m'],[45,90,'os sacrum','k']])
f('4-3',5,cap='M. longissimus (rdeče) – srednji steber m. erector spinae; najdaljši, sega od križnice do processus mastoideus (longissimus capitis).',a=[
 [44,12,'m. longissimus capitis / cervicis','m'],[43,45,'m. longissimus thoracis','m'],[30,85,'crista iliaca','k'],[42,80,'os sacrum','k']])
f('4-3',6,cap='M. spinalis – najbolj medialni steber m. erector spinae: od trna do trna (spinalis thoracis T10–L2 → T2–T8).',a=[
 [48,30,'m. spinalis','m'],[50,75,'processus spinosus','k'],[30,30,'scapula','k']])
f('4-3',7,cap='Mm. transversospinales (najgloblji sloj, od prečnega odrastka navzgor na trn): m. semispinalis (preskoči 4–6 vretenc), m. multifidus (2–4, najmočnejši v ledvenem delu), mm. rotatores (1–2).',a=[
 [49,25,'m. semispinalis','m'],[49,70,'m. multifidus','m'],[54,70,'mm. rotatores','m'],[50,8,'m. semispinalis capitis','m']])
f('4-3',8,cap='Mm. suboccipitales (najgloblje pod zatilnico): rectus capitis posterior major in minor, obliquus capitis superior in inferior; omejujejo trigonum suboccipitale, skozi katerega poteka a. vertebralis. Fina kontrola drže glave.',a=[
 [40,32,'m. rectus capitis posterior major','m'],[30,30,'m. obliquus capitis superior','m'],[38,47,'a. vertebralis – trigonum suboccipitale','z'],
 [40,55,'m. obliquus capitis inferior','m'],[47,32,'m. rectus capitis posterior minor','m'],[50,63,'processus spinosus axis (C2)','k']])
f('4-4',1,cap='Trebušna stena po plasteh (levo odstranjeni): m. obliquus externus (najbolj zunaj) → m. obliquus internus → m. transversus abdominis (najgloblje); spredaj m. rectus abdominis v ovojnici, med obema linea alba.',a=[
 [43,43,'m. transversus abdominis – najgloblja','m'],[38,50,'m. obliquus internus abdominis','m'],[36,60,'m. obliquus externus abdominis','m'],
 [56,45,'m. rectus abdominis','m'],[51,35,'linea alba','s'],[55,24,'intersectio tendinea','s'],[51,55,'umbilicus – popek','o'],[66,30,'m. obliquus externus (desno)','m']])
f('4-4',2,cap='Smer vlaken: externus poteka navzdol-medialno (»roke v žepih«), internus navzgor-medialno (pravokotno nanj), transversus prečno. Rectus abdominis je razdeljen z intersectiones tendineae (»six pack«).',a=[
 [43,45,'m. transversus abdominis – najgloblja','m'],[37,52,'m. obliquus internus','m'],[54,47,'m. rectus abdominis','m'],[64,38,'m. obliquus externus','m'],
 [50,40,'linea alba','s'],[55,37,'intersectio tendinea','s']])
f('4-4',3,cap='M. obliquus internus abdominis: origo – fascia thoracolumbalis, crista iliaca, lateralni del lig. inguinale; insertio – spodnja 3–4 rebra, aponevroza v linea alba. Fleksija in rotacija trupa na isto stran.',a=[
 [37,45,'m. obliquus internus abdominis','m'],[62,45,'m. obliquus internus (vlakna navzgor-medialno)','m'],[36,30,'spodnja rebra – insertio','k'],[33,57,'crista iliaca – origo','k'],[41,73,'lig. inguinale – origo','s']])
f('4-4',4,cap='M. transversus abdominis (rjavo): origo – notranja stran hrustancev reber 7–12, fascia thoracolumbalis, crista iliaca, lig. inguinale; insertio – linea alba. Vlakna prečno; »naravni steznik« – stabilizacija ledvene hrbtenice, povečanje trebušnega tlaka.',a=[
 [50,57,'m. transversus abdominis – prečna vlakna','m'],[56,48,'rebra 7–12 – origo','k'],[52,80,'crista iliaca – origo','k'],[41,50,'linea alba / ovojnica recta – insertio','s']])
f('4-4',5,cap='M. rectus abdominis: origo – symphysis in crista pubica; insertio – processus xiphoideus in hrustanci 5.–7. rebra. Fleksija trupa. Desno: kolčnica s kostnimi točkami, ki jih rabiš za narastišča trebušnih in kolčnih mišic.',a=[
 [17,37,'m. rectus abdominis','m'],[71,8,'crista iliaca','k'],[78,30,'spina iliaca anterior superior (SIAS)','k'],[77,48,'spina iliaca anterior inferior','k'],
 [73,63,'acetabulum','s'],[93,68,'tuberculum pubicum','k'],[80,75,'foramen obturatum','k'],[72,88,'tuber ischiadicum','k'],[86,60,'ramus superior ossis pubis','k']])
f('4-4',6,cap='M. quadratus lumborum (zeleno): origo – crista iliaca (zadnji del) in lig. iliolumbale; insertio – 12. rebro in procc. transversi L1–L4. Lateralna fleksija trupa, fiksira 12. rebro pri vdihu.',a=[
 [40,48,'m. quadratus lumborum','m'],[39,36,'costa XII – insertio','k'],[52,40,'processus transversi L1–L4 – insertio','k'],[37,62,'crista iliaca – origo','k']])
f('4-5',1,cap='Prsni koš od spredaj: levo površinsko m. pectoralis major, desno odstranjen – pod njim m. pectoralis minor in m. subclavius; v sulcus deltoideopectoralis poteka v. cephalica.',a=[
 [42,13,'m. sternocleidomastoideus','m'],[35,26,'trigonum deltoideopectorale','o'],[29,33,'v. cephalica','z'],[38,46,'m. pectoralis major','m'],
 [27,63,'v. axillaris','z'],[62,22,'m. subclavius','m'],[85,28,'m. deltoideus','m'],[79,53,'v. axillaris','z'],[72,48,'m. pectoralis minor','m'],[60,70,'mm. intercostales externi','m'],[48,20,'clavicula','k']])
f('4-5',2,cap='M. pectoralis major: tri porcije – clavicularis (medialna polovica ključnice), sternocostalis (sternum, rebrni hrustanci 1–6), abdominalis (ovojnica recta); insertio – crista tuberculi majoris. Addukcija, notranja rotacija, fleksija (klavikularni del). Desno: kostne točke humerusa.',a=[
 [14,15,'pars clavicularis','m'],[22,29,'pars sternocostalis','m'],[21,42,'pars abdominalis','m'],[33,62,'caput claviculare','m'],[39,72,'caput sternocostale','m'],
 [70,61,'tuberculum majus','k'],[77,62,'tuberculum minus','k'],[74,64,'sulcus intertubercularis','k'],[72,72,'crista tuberculi majoris – insertio','k'],
 [77,72,'crista tuberculi minoris','k'],[74,90,'tuberositas deltoidea','k']])
f('4-5',3,cap='Funkcija m. pectoralis major pri vadbi: horizontalna addukcija (križanje rok spredaj); zgornji (klavikularni) del sodeluje s sprednjim deltoidom pri dvigu, spodnji pri potisku navzdol.',a=[
 [31,7,'m. deltoideus – pars anterior','m'],[35,9,'pectoralis major – zgornji (klavikularni) del','m'],[38,12,'pectoralis major – spodnji (sternokostalni) del','m'],[27,13,'m. biceps brachii – caput breve','m'],
 [32,62,'m. deltoideus – pars anterior','m'],[33,67,'pectoralis major – zgornji del','m'],[34,71,'pectoralis major – spodnji del','m'],[29,71,'m. latissimus dorsi','m']])
f('4-5',4,cap='M. pectoralis minor (rdeče): origo – rebra 3–5; insertio – processus coracoideus scapulae (desno rdeče). Spusti in potegne lopatico naprej; pri fiksirani lopatici dvigne rebra (pomožna vdihalka).',a=[
 [34,41,'m. pectoralis minor','m'],[27,45,'rebra 3–5 – origo','k'],[94,59,'processus coracoideus – insertio','k'],[83,70,'scapula','k']])
f('4-5',5,cap='M. serratus anterior: origo – rebra 1–8/9 (nazobčano); insertio – margo medialis scapulae (sprednja stran). Protrakcija lopatice in rotacija navzgor (dvig roke nad glavo); drži lopatico ob prsnem košu – okvara n. thoracicus longus → »krilata lopatica«.',a=[
 [30,50,'m. serratus anterior','m'],[19,50,'margo medialis scapulae – insertio','k'],[41,44,'rebra 1–9 – origo (nazobčano)','k'],[74,48,'m. serratus anterior','m'],[66,40,'scapula','k']])
f('4-5',6,cap='Medrebrne mišice: externi (vlakna navzdol naprej – vdih), interni (navzgor naprej – izdih), intimi (najgloblje). Desno spodaj m. transversus thoracis na zadnji strani prsnice.',a=[
 [8,15,'m. intercostalis intimus – najgloblje','m'],[17,28,'m. intercostalis internus','m'],[31,22,'m. intercostalis externus','m'],
 [12,70,'mm. intercostales externi – navzdol naprej','m'],[48,84,'mm. intercostales interni – navzgor naprej','m'],[80,61,'m. transversus thoracis','m'],[86,57,'facies posterior sterni','k']])
f('4-5',7,cap='Medrebrni prostor: m. intercostalis externus (zunaj), internus, intimus (najgloblje); med internusom in intimusom žilno-živčni snop v sulcus costae (od zgoraj: vena, arterija, živec – VAN). Spredaj externus preide v membrano intercostalis externa.',a=[
 [12,35,'m. intercostalis externus','m'],[30,32,'v. intercostalis','z'],[30,34,'a. intercostalis','z'],[30,37,'n. intercostalis','z'],
 [22,47,'m. intercostalis internus','m'],[28,47,'m. intercostalis intimus','m'],[67,63,'membrana intercostalis externa','s'],[55,62,'m. intercostalis externus','m'],[75,40,'sternum','k']])
f('4-5',8,cap='M. transversus thoracis (zadnja stran sprednje prsne stene): od spodnjega dela prsnice na hrustance 2.–6. rebra; spušča rebra (izdih). Ob prsnici vasa thoracica interna.',a=[
 [50,22,'vasa thoracica interna','z'],[60,40,'sternum','k'],[48,52,'m. transversus thoracis','m'],[40,76,'diaphragma','m'],[61,83,'sternalni izvor prepone','m'],[34,89,'m. transversus abdominis','m'],[30,58,'mm. intercostales interni','m']])
f('4-5',9,cap='Trebušna prepona od spredaj: desna kupola stoji višje (pod njo jetra), leva nižje; kraka (crura) se pripenjata na ledvena vretenca – desni na L1–L3, levi na L1–L2.',a=[
 [26,56,'desna kupola – stoji višje','m'],[78,60,'leva kupola','m'],[50,52,'processus xiphoideus','k'],[51,80,'crus dextrum','m'],[57,77,'crus sinistrum','m']])
f('4-5',10,cap='Prepona od spodaj: centrum tendineum v sredini, mišični deli (sternalni, kostalni, ledveni). Odprtine – »I 8 10 Eggs At 12«: v. cava T8, oesophagus T10, aorta T12. Crura in ligg. arcuata (mediale čez psoas, laterale čez quadratus lumborum).',a=[
 [50,10,'processus xiphoideus','k'],[45,14,'pars sternalis','m'],[42,15,'trigonum sternocostale (Morgagni)','o'],[62,22,'pars costalis','m'],
 [40,37,'foramen venae cavae (T8)','z'],[52,32,'centrum tendineum','s'],[52,42,'hiatus oesophageus (T10)','z'],[50,57,'hiatus aorticus (T12)','z'],
 [42,58,'crus dextrum','m'],[54,64,'crus sinistrum','m'],[74,76,'lig. arcuatum laterale','s'],[60,73,'lig. arcuatum mediale','s'],[25,78,'m. quadratus lumborum','m'],[34,80,'m. psoas major','m'],[46,94,'columna vertebralis lumbalis','k']])
f('4-5',11,cap='Dihalne mišice. Vdih – glavne: diaphragma in mm. intercostales externi; pomožne: SCM, mm. scaleni (in pectoralis minor). Izdih – mirni je pasiven (elastičnost pljuč); aktivni: mm. intercostales interni in trebušne mišice.',a=[
 [42,9,'m. sternocleidomastoideus – vdih, pomožna','m'],[40,19,'mm. scaleni – vdih, pomožna','m'],[34,47,'mm. intercostales externi – vdih','m'],
 [31,62,'diaphragma – glavna mišica vdiha','m'],[67,48,'mm. intercostales interni – aktivni izdih','m'],[58,62,'trebušne mišice – aktivni izdih','m']])
f('4-6',1,cap='(a) Levo površinsko: m. deltoideus in m. latissimus dorsi. (b) Globoko (odstranjen deltoid): m. supraspinatus nad spino, m. infraspinatus pod njo, m. teres minor in major ob lateralnem robu, m. triceps brachii na nadlakti.',a=[
 [17,24,'m. deltoideus','m'],[22,50,'m. latissimus dorsi','m'],[67,22,'m. teres minor','m'],[70,11,'m. supraspinatus','m'],[73,15,'spina scapulae','k'],
 [72,25,'m. deltoideus (prerezan)','m'],[73,30,'m. infraspinatus','m'],[68,43,'m. teres major','m'],[56,36,'humerus','k'],[61,46,'m. triceps – caput longum','m'],[58,60,'m. triceps – caput laterale','m'],[69,48,'m. latissimus dorsi (blizu izvora)','m']])
f('4-6',2,cap='Ramenske mišice od zadaj: levo površinske (deltoideus, latissimus dorsi), desno globoke – rotatorna manšeta (supraspinatus, infraspinatus, teres minor) in teres major; na nadlakti triceps.',a=[
 [22,38,'m. deltoideus','m'],[30,34,'m. supraspinatus','m'],[27,47,'m. teres major','m'],[40,70,'m. latissimus dorsi','m'],
 [62,40,'m. infraspinatus','m'],[70,37,'m. teres minor','m'],[76,55,'m. triceps brachii','m']])
f('4-6',3,cap='M. deltoideus (zgoraj rdeče): origo – lateralna tretjina ključnice, akromion, spina scapulae; insertio – tuberositas deltoidea (spodaj zeleno). Glavni abduktor nadlakti (15–90°). Sredina: deli lopatice od zadaj.',a=[
 [43,16,'m. deltoideus','m'],[49,37,'margo superior','k'],[44,41,'fossa supraspinata','k'],[43,45,'spina scapulae','k'],[60,37,'processus coracoideus','k'],
 [59,41,'acromion','k'],[47,51,'fossa infraspinata','k'],[56,46,'cavitas glenoidalis (angulus lateralis)','s'],[41,55,'margo medialis','k'],[54,55,'margo lateralis','k'],[46,81,'tuberositas deltoidea – insertio','k']])
f('4-6',4,cap='M. teres minor in m. teres major od zadaj. Pozor: teres minor (del rotatorne manšete) gre na tuberculum majus in rotira navzven; teres major (ni del manšete) gre na crista tuberculi minoris in rotira navznoter. Med njima poteka caput longum m. triceps.',a=[
 [35,18,'m. supraspinatus','m'],[50,22,'spina scapulae','k'],[30,45,'m. infraspinatus','m'],[61,39,'m. teres minor','m'],[37,62,'m. teres major','m'],[58,70,'m. triceps – caput longum','m']])
f('4-6',5,cap='M. supraspinatus – origo fossa supraspinata, insertio zgornja ploskev tuberculum majus; začne abdukcijo nadlakti. Pri utesnitvi pod akromionom se njegova kita najpogosteje poškoduje.',a=FIX['2-3'][2]['a'])
f('4-6',6,cap='M. infraspinatus: origo – fossa infraspinata; insertio – srednja ploskev tuberculum majus. Glavni zunanji rotator nadlakti. Oživčenje: n. suprascapularis.',a=[
 [43,19,'m. infraspinatus (rdeče)','m'],[57,55,'tuberculum majus – insertio','k'],[50,63,'m. infraspinatus','m'],[47,72,'fossa infraspinata – origo','k']])
f('4-6',7,cap='Zgoraj: teres minor nad teres major. Spodaj: m. teres minor (zeleno) – origo margo lateralis scapulae, insertio spodnja ploskev tuberculum majus, zunanja rotacija (n. axillaris). Pod njim m. teres major.',a=[
 [47,18,'m. teres minor','m'],[44,28,'m. teres major','m'],[52,60,'m. teres minor (zeleno)','m'],[38,82,'m. teres major','m'],[58,80,'m. triceps – caput longum','m'],[55,43,'caput humeri','k']])
f('4-6',9,cap='Rotatorna manšeta »SITS«: Supraspinatus (zgornja ploskev tub. majus), Infraspinatus (srednja), Teres minor (spodnja) – zunanji rotatorji; Subscapularis (tuberculum minus, spredaj) – notranji rotator. Skupaj držijo glavico humerusa v plitvi ponvici.',a=[
 [45,23,'S · m. supraspinatus','m'],[40,42,'I · m. infraspinatus','m'],[42,58,'T · m. teres minor','m'],[79,44,'S · m. subscapularis (spredaj)','m'],
 [41,75,'scapula','k'],[72,82,'humerus','k'],[73,30,'acromion','k']])
f('4-6',10,cap='Sprednja stran nadlakti: m. biceps brachii – caput breve (processus coracoideus) in caput longum (tuberculum supraglenoidale, kita skozi sulcus intertubercularis); insertio tuberositas radii. Fleksija komolca in supinacija. Pod njim m. brachialis.',a=[
 [42,25,'m. biceps – caput breve','m'],[52,37,'m. biceps – caput longum','m'],[56,84,'m. brachialis','m'],[34,30,'m. pectoralis minor','m'],[40,14,'processus coracoideus','k']])
f('4-6',11,cap='M. brachialis (pod bicepsom, zeleno): origo – sprednja stran distalne polovice humerusa; insertio – tuberositas ulnae. Najmočnejši čisti fleksor komolca (deluje ne glede na pronacijo/supinacijo). Oživčenje: n. musculocutaneus.',a=[
 [50,24,'m. biceps brachii','m'],[46,38,'m. brachialis','m'],[37,80,'m. brachialis (zeleno)','m'],[36,60,'humerus','k']])
f('4-6',8,cap='M. subscapularis: origo – fossa subscapularis (modro, sprednja stran lopatice); insertio – tuberculum minus humeri. Notranji rotator, edini »S« manšete spredaj. Spodaj: kostne točke proksimalnega humerusa.',a=[
 [49,5,'acromion','k'],[44,12,'processus coracoideus','k'],[45,21,'cavitas glenoidalis','s'],[30,45,'fossa subscapularis – origo','k'],
 [28,72,'tuberculum majus','k'],[38,71,'caput humeri','s'],[31,76,'sulcus intertubercularis','k'],[35,75,'tuberculum minus – insertio m. subscapularis','k'],
 [37,73,'collum anatomicum','k'],[34,82,'collum chirurgicum','k'],[29,88,'crista tuberculi majoris','k'],[63,73,'caput humeri (od zadaj)','s'],[71,73,'tuberculum majus','k']])
f('4-6',12,cap='M. coracobrachialis: origo – processus coracoideus; insertio – medialna stran sredine humerusa (zeleno). Fleksija in addukcija nadlakti. Prebada ga n. musculocutaneus.',a=[
 [29,24,'m. coracobrachialis','m'],[52,56,'processus coracoideus – origo','k'],[42,85,'insertio – medialna stran humerusa','k']])
f('4-6',13,cap='M. triceps brachii: caput longum (tuberculum infraglenoidale – edina glava, ki prečka ramenski sklep), caput laterale in mediale (zadnja stran humerusa); insertio – olecranon. Ekstenzija komolca. Oživčenje: n. radialis.',a=[
 [44,17,'tuberculum infraglenoidale – origo c. longum','k'],[47,28,'caput longum','m'],[54,28,'caput laterale','m'],[51,42,'caput mediale','m'],[53,80,'olecranon – insertio','k']])
f('1-4',8,skip=True)
f('3-2',3,cap='Medvretenčni stik (symphysis) in vratno vretence – ponovitev: discus intervertebralis z nucleus pulposus in anulus fibrosus.',a=FIX['2-2'][2]['a'])
f('3-8',2,cap='Lobanjsko dno od spodaj – ponovitev s slike 2: narastišča žvekalnih in vratnih mišic (processus pterygoideus – mm. pterygoidei; processus mastoideus – SCM; processus styloideus – m. stylohyoideus).',a=FIX['2-1'][2]['a'])
