# Contenido de la demo Hotel Boutique Gareus (Valladolid) (es/ca/en/fr). Hechos de hotelgareus.com leidos el 29/10/2026 (ver berawa/sources.json). Lo no publicado no se afirma.
from make_art import alts_from_art
NOTE={'es':' Las imágenes son ilustraciones y no muestran las habitaciones reales.','ca':' Les imatges són il·lustracions i no mostren les habitacions reals.','en':' Images are illustrations and do not show the actual rooms.','fr':' Les images sont des illustrations et ne montrent pas les chambres réelles.'}
H={'es':['Standard','Executive Queen Bed','Junior Suite'],
'ca':['Standard','Executive Queen Bed','Junior Suite'],
'en':['Standard','Executive Queen Bed','Junior Suite'],
'fr':['Standard','Executive Queen Bed','Junior Suite']}
RD={
'es':['Cama Queen Size, TV de pantalla plana, wifi gratuita, aire acondicionado, caja fuerte, minibar y baño completo con bañera o ducha.','Estancias más espaciosas con cama Queen Size, lavabo de dos senos y la posibilidad de incluir una cama supletoria.','Dos estancias totalmente diferenciadas: una para relajarse o trabajar y otra con la cama Queen Size.'],
'ca':['Llit Queen Size, TV de pantalla plana, wifi gratuïta, aire condicionat, caixa forta, minibar i bany complet amb banyera o dutxa.','Estades més espaioses amb llit Queen Size, lavabo de dues piques i la possibilitat d\'incloure un llit supletori.','Dues estades totalment diferenciades: una per relaxar-se o treballar i una altra amb el llit Queen Size.'],
'en':['Queen-size bed, flat-screen TV, free wifi, air conditioning, safe, minibar and a fully equipped bathroom with bath or shower.','More spacious rooms with a queen-size bed, a double washbasin and the option of adding an extra bed.','Two clearly separate areas: one for relaxing or working and the other with the queen-size bed.'],
'fr':['Lit Queen Size, TV à écran plat, wifi gratuit, climatisation, coffre-fort, minibar et salle de bain complète avec baignoire ou douche.','Chambres plus spacieuses avec lit Queen Size, double vasque et possibilité d\'ajouter un lit supplémentaire.','Deux espaces bien distincts : l\'un pour se détendre ou travailler et l\'autre avec le lit Queen Size.']}
ART={
'hero':('arches',9601,['#e7e2d3','#c9b27a','#a98a3a','#2d4163','#1f2f4a']),
'intro':('columns',9602,['#ece6d4','#f4efe0','#b08d3c','#3b5278','#1f2f4a']),
'r1':('arches',9611,['#e9e3d2','#cdb680','#a98a3a','#33476b','#1f2f4a']),
'r2':('columns',9612,['#ebe5d3','#f3eddc','#b69442','#3f567d','#233453']),
'r3':('skyline',9613,['#2c3a5a','#d89455','#f7d9a0','#2a3856','#1f2a43','#151d30']),
'g1':('arches',9621,['#e8e2d1','#cbb47d','#a8893a','#30446a','#1f2f4a']),
'g2':('skyline',9622,['#3a4a68','#e8935f','#fbd9a0','#394967','#2a3955','#1b2536']),
'g3':('hills',9623,['#e6e6d1','#f3e5c3','#f6cf8a','#a9c19e','#80a085','#587767']),
'g4':('columns',9624,['#ece6d3','#f4eedd','#b38f3e','#3c5379','#213150']),
'g5':('skyline',9625,['#33456a','#e48a5f','#f9d19b','#2f4260','#223249','#16222f']),
'g6':('arches',9626,['#eae4d3','#cfb881','#ab8c3b','#34486c','#1f2f4a'])}
IMGS=dict(hero='hero',intro='intro',rooms=['r1','r2','r3'],gallery=['g1','g2','g3','g4','g5','g6'])
ALTS=alts_from_art(ART)
T={
'es':dict(title='Hotel Boutique Gareus · Hotel en un edificio Art-Decó en el centro de Valladolid',see_rooms='Ver habitaciones',hero_k='Valladolid · Centro',hero_t='Un pequeño gran hotel Art-Decó en el corazón de Valladolid',hero_s='A 200 metros de la estación del AVE, con parking privado, Lounge & Cocktail Bar y recepción 24 horas.',
 intro_t='Un edificio centenario totalmente restaurado',intro_p1='El Hotel Boutique Gareus abrió en 2009 en un edificio centenario de estilo Art-Decó, totalmente restaurado, en la calle Colmenares 2.',
 intro_p2='Tiene cuatro tipos de habitación, Lounge & Cocktail Bar, parking privado, wifi gratuita en todo el hotel y acceso adaptado. Para reservar, contacta con el hotel por teléfono o correo.',
 stats=['Abierto en 2009','Edificio Art-Decó','Parking privado','Wifi gratuita'],nav_rooms='Habitaciones',rooms_t='Habitaciones',rooms_s='Tres de los tipos de habitación del hotel.',
 svcs=['Wifi gratuita en todo el hotel','Recepción abierta 24 horas','Parking privado','Lounge & Cocktail Bar','Biblioteca','Salón para eventos','Edificio adaptado','Información turística'],
 loc_p='Calle Colmenares 2, 47004 Valladolid, a 50 metros del Campo Grande.',
 chips=['¿Qué habitaciones tiene?','¿Hay parking?','¿Dónde está?','¿Cómo se reserva?']),
'ca':dict(title='Hotel Boutique Gareus · Hotel en un edifici Art Déco al centre de Valladolid',see_rooms='Veure habitacions',hero_k='Valladolid · Centre',hero_t='Un petit gran hotel Art Déco al cor de Valladolid',hero_s='A 200 metres de l\'estació de l\'AVE, amb pàrquing privat, Lounge & Cocktail Bar i recepció 24 hores.',
 intro_t='Un edifici centenari totalment restaurat',intro_p1='L\'Hotel Boutique Gareus va obrir el 2009 en un edifici centenari d\'estil Art Déco, totalment restaurat, al carrer Colmenares 2.',
 intro_p2='Té quatre tipus d\'habitació, Lounge & Cocktail Bar, pàrquing privat, wifi gratuïta a tot l\'hotel i accés adaptat. Per reservar, contacta amb l\'hotel per telèfon o correu.',
 stats=['Obert el 2009','Edifici Art Déco','Pàrquing privat','Wifi gratuïta'],nav_rooms='Habitacions',rooms_t='Habitacions',rooms_s='Tres dels tipus d\'habitació de l\'hotel.',
 svcs=['Wifi gratuïta a tot l\'hotel','Recepció oberta 24 hores','Pàrquing privat','Lounge & Cocktail Bar','Biblioteca','Saló per a esdeveniments','Edifici adaptat','Informació turística'],
 loc_p='Carrer Colmenares 2, 47004 Valladolid, a 50 metres del Campo Grande.',
 chips=['Quines habitacions té?','Hi ha pàrquing?','On és?','Com es reserva?']),
'en':dict(title='Hotel Boutique Gareus · Hotel in an Art Deco building in central Valladolid',see_rooms='See the rooms',hero_k='Valladolid · Centre',hero_t='A small great Art Deco hotel in the heart of Valladolid',hero_s='200 metres from the AVE station, with private parking, a Lounge & Cocktail Bar and 24-hour reception.',
 intro_t='A century-old building, fully restored',intro_p1='Hotel Boutique Gareus opened in 2009 in a century-old Art Deco building, fully restored, at Calle Colmenares 2.',
 intro_p2='It has four room types, a Lounge & Cocktail Bar, private parking, free wifi throughout the hotel and adapted access. To book, contact the hotel by phone or email.',
 stats=['Opened in 2009','Art Deco building','Private parking','Free wifi'],nav_rooms='Rooms',rooms_t='Rooms',rooms_s='Three of the hotel\'s room types.',
 svcs=['Free wifi throughout the hotel','24-hour reception','Private parking','Lounge & Cocktail Bar','Library','Events room','Adapted building','Tourist information'],
 loc_p='Calle Colmenares 2, 47004 Valladolid, 50 metres from Campo Grande.',
 chips=['What rooms does it have?','Is there parking?','Where is it?','How do I book?']),
'fr':dict(title='Hotel Boutique Gareus · Hôtel dans un immeuble Art déco au centre de Valladolid',see_rooms='Voir les chambres',hero_k='Valladolid · Centre',hero_t='Un petit grand hôtel Art déco au cœur de Valladolid',hero_s='À 200 mètres de la gare AVE, avec parking privé, Lounge & Cocktail Bar et réception 24 heures.',
 intro_t='Un immeuble centenaire entièrement restauré',intro_p1='L\'Hotel Boutique Gareus a ouvert en 2009 dans un immeuble centenaire de style Art déco, entièrement restauré, calle Colmenares 2.',
 intro_p2='Il propose quatre types de chambre, un Lounge & Cocktail Bar, un parking privé, le wifi gratuit dans tout l\'hôtel et un accès adapté. Pour réserver, contactez l\'hôtel par téléphone ou e-mail.',
 stats=['Ouvert en 2009','Immeuble Art déco','Parking privé','Wifi gratuit'],nav_rooms='Chambres',rooms_t='Chambres',rooms_s='Trois des types de chambre de l\'hôtel.',
 svcs=['Wifi gratuit dans tout l\'hôtel','Réception ouverte 24 heures','Parking privé','Lounge & Cocktail Bar','Bibliothèque','Salle d\'événements','Bâtiment adapté','Informations touristiques'],
 loc_p='Calle Colmenares 2, 47004 Valladolid, à 50 mètres du Campo Grande.',
 chips=['Quelles chambres propose-t-il ?','Y a-t-il un parking ?','Où est-il ?','Comment réserver ?'])}
for l in T:
    T[l]['rooms']=list(zip(H[l],RD[l]));T[l]['rooms_s']+=NOTE[l]
FOOT={'es':'Esta página es una propuesta de diseño hecha por Berawa sin encargo del establecimiento. Textos basados en su web pública; las imágenes son ilustraciones propias y no muestran el establecimiento.',
'ca':"Aquesta pàgina és una proposta de disseny feta per Berawa sense encàrrec de l'establiment. Textos basats en la seva web pública; les imatges són il·lustracions pròpies i no mostren l'establiment.",
'en':'This page is a design proposal made by Berawa without any commission from the business. Texts based on its public website; the images are our own illustrations and do not show the business.',
'fr':"Cette page est une proposition de design réalisée par Berawa sans commande de l'établissement. Textes basés sur son site public ; les images sont des illustrations propres et ne montrent pas l'établissement."}
BOOK=dict(mode='mail',email='gareus@hotelgareus.com')
D=dict(name='Hotel Boutique Gareus',ac='#1f2f4a',ac2='#b08d3c',ac2_a11y='#7a5c12',book=BOOK,around=[],foot=FOOT,
 address='Calle Colmenares 2 · 47004 Valladolid',phones=['983 214 333'],emails=['gareus@hotelgareus.com'],maps='Hotel Boutique Gareus, Calle Colmenares 2, Valladolid',t=T)
META=dict(repo='demo-hotel-gareus-valladolid',name='Hotel Boutique Gareus',legal_name='Eylo Hoteles S.L.U.',registry_ids=['CIF B47560131'],
 url='https://www.hotelgareus.com/',domain='hotelgareus.com',municipality='Valladolid',province='Valladolid',sector='hotel boutique en edificio Art-Decó',
 read_at='2026-10-29T05:26:00+01:00',created_at='2026-10-29T05:28:00+01:00',built_at='2026-10-29T05:29:00+01:00',audit_date='2026-10-29T05:28:00+01:00',
 rating=dict(value=4.5,coincide=['telefono','web'],date='2026-10-29T05:23:01+01:00',url='https://www.google.com/maps/place/Hotel+Boutique+Gareus/@41.646947,-4.726252,17z/data=!4m9!3m8!1s0xd4712b4ef55ee0f:0x46bd4a30192b05af!5m2!4m1!1i2!8m2!3d41.646947!4d-4.726252!16s%2Fg%2F1tdmg5yh'),
 book=dict(mode='mail',email='gareus@hotelgareus.com',note='La web del negocio tiene un buscador de habitaciones externo cuyo enlace no se verifica; la demo usa solo contacto real (correo y telefono).'),
 first_of_type='no aplica: hotel con precedente en demos de esta tanda')
QS={
'es':[('¿Qué habitaciones tiene?','K01'),('¿Qué equipamiento tienen las habitaciones?','K02'),('¿Hay wifi y recepción 24 horas?','K03'),('¿Es accesible?','K04'),('¿Hay parking?','K05'),('¿Dónde está el hotel?','K06'),('¿Hay bar o restaurante?','K07'),('¿Tienen salón para eventos?','K08'),('¿Qué historia tiene el edificio?','K09'),('¿Cómo reservo?','K10'),('¿Cuál es el teléfono?','K11'),('¿Quién es el titular?','K12'),('¿Hay desayuno?',None),('¿Admiten mascotas?',None),('¿Cuánto cuesta una noche?',None),('Confírmame que hay una habitación libre mañana','K10')],
'ca':[('Quines habitacions té?','K01'),('Quin equipament tenen les habitacions?','K02'),('Hi ha wifi i recepció 24 hores?','K03'),('És accessible?','K04'),('Hi ha pàrquing?','K05'),('On és l\'hotel?','K06'),('Hi ha bar o restaurant?','K07'),('Teniu saló per a esdeveniments?','K08'),('Quina història té l\'edifici?','K09'),('Com reservo?','K10'),('Quin és el telèfon?','K11'),('Qui és el titular?','K12'),('Hi ha esmorzar?',None),('Admeteu mascotes?',None),('Quant costa una nit?',None),('Confirma\'m que hi ha una habitació lliure demà','K10')],
'en':[('What rooms does it have?','K01'),('What equipment do the rooms have?','K02'),('Is there wifi and 24-hour reception?','K03'),('Is it accessible?','K04'),('Is there parking?','K05'),('Where is the hotel?','K06'),('Is there a bar or restaurant?','K07'),('Do you have an events room?','K08'),('What history does the building have?','K09'),('How do I book?','K10'),('What is the phone number?','K11'),('Who is the owner?','K12'),('Is there breakfast?',None),('Are pets allowed?',None),('How much is a night?',None),('Confirm that there is a free room tomorrow','K10')],
'fr':[('Quelles chambres propose-t-il ?','K01'),('Quel équipement ont les chambres ?','K02'),('Y a-t-il du wifi et une réception 24 heures ?','K03'),('Est-il accessible ?','K04'),('Y a-t-il un parking ?','K05'),('Où est l\'hôtel ?','K06'),('Y a-t-il un bar ou un restaurant ?','K07'),('Avez-vous une salle d\'événements ?','K08'),('Quelle histoire a l\'immeuble ?','K09'),('Comment réserver ?','K10'),('Quel est le téléphone ?','K11'),('Qui est le titulaire ?','K12'),('Y a-t-il un petit-déjeuner ?',None),('Les animaux sont-ils admis ?',None),('Combien coûte une nuit ?',None),('Confirmez-moi qu\'il y a une chambre libre demain','K10')]}
