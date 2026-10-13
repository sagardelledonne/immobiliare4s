# Prodotti Bosari: dati ricavati dalle pagine prodotto del sito attuale (screenshot forniti dal cliente).
# Il sito originale e' solo in inglese: le versioni italiane sono traduzioni da far rivedere al cliente.
# Un valore scritto come stringa semplice e' uguale nelle due lingue; come {"it":..., "en":...} cambia.

def L(it, en):
    return {"it": it, "en": en}


# ---- famiglie ---------------------------------------------------------------
FAMILIES = [
    {
        "id": "atlantis",
        "name": "ATLANTIS®",
        "title": L("Raffreddatori ad acqua", "Water coolers"),
        "intro": L(
            "Raffreddatori ad acqua in alluminio per tiristori, GTO e IGBT: fino a 4.000 W dissipati sulle due facce.",
            "Aluminium water coolers for thyristors, GTOs and IGBTs: up to 4,000 W dissipated on both sides.",
        ),
        "products": ["bae6", "bae9"],
    },
    {
        "id": "columbus",
        "name": "COLUMBUS",
        "title": L("Scambiatori di calore per armadi elettronici", "Heat exchangers for electronic cabinets"),
        "intro": L(
            "Scambiatori controcorrente a circuiti separati, senza scambio d'aria tra armadio e ambiente, conformi a IP55 e NEMA 12.",
            "Counterflow exchangers with separated circuits and no air exchange between cabinet and ambient, compliant with IP55 and NEMA 12.",
        ),
        "products": ["columbus1000"],
    },
    {
        "id": "ucool",
        "name": "U-COOL®",
        "title": L("Sistemi di raffreddamento a heat pipe", "Heat pipe cooling systems"),
        "intro": L(
            "Raffreddatori a heat pipe a convezione naturale, nati per l'elettronica di potenza sui veicoli ferroviari.",
            "Natural-convection heat pipe coolers, designed for power electronics on railway vehicles.",
        ),
        "products": ["ucool1200"],
    },
]

# ---- testo comune ATLANTIS ----------------------------------------------------
ATLANTIS_TEXT = {
    "it": [
        "Negli ultimi anni lo sviluppo dei componenti elettronici di potenza ha reso necessario dissipare quantità sempre maggiori di calore, per mantenere basse le temperature di giunzione e aumentarne la vita operativa.",
        "I progettisti hanno preso sempre più confidenza con i sistemi di raffreddamento alternativi, come il raffreddamento ad acqua, che hanno dimostrato la massima affidabilità in condizioni ambientali severe.",
        "Per rispondere ai problemi di elevata dissipazione, Bosari Thermal Management (BTM) ha progettato e sviluppato una nuova famiglia di raffreddatori ad acqua in alluminio, adatti a tiristori, GTO e ai recenti componenti IGBT, {power}",
        "Questa famiglia si adatta facilmente alle esigenze del cliente, montando il raccordo per il fluido più adatto (alluminio, titanio, ecc.).",
        "Il concetto costruttivo rende questi raffreddatori molto convenienti e ne allunga la vita operativa a un prezzo ragionevole: per questo si adottano nella maggior parte delle applicazioni industriali pesanti, nella saldatura e nella trazione elettrica leggera e pesante.",
    ],
    "en": [
        "During the course of recent years the development of electronic power components has made necessary to dissipate larger quantities of thermal heat at lower values of junction temperatures in order to increase their operating life.",
        "The designers have become more and more familiar with alternative cooling systems, such as water cooling, that have shown the highest reliability in severe environmental conditions.",
        "As an answer to high power dissipation problems, Bosari Thermal Management (BTM) has designed and developed a new family of aluminium water coolers, suitable to accept Thyristors, GTOs, and the recent IGBT components, {power}",
        "This new cooler family can be easily adapted to the customer needs, by mounting the proper cooling fluid nipple (aluminium, titanium, etc.).",
        "The basic concept of these coolers makes them really cost-effective, allowing a longer operating life to the components at a really reasonable price, thus permitting to adopt them in the most part of heavy industrial applications, welding, light and heavy electrical traction.",
    ],
}


def _atlantis_specs(rth1, rth2, force, weight):
    return [
        (L("Termiche", "Thermal"), [
            (L("Rth (un lato) @6 l/min", "Rth (single side) @6 l/min"), rth1),
            (L("Rth (due lati) @6 l/min", "Rth (double side) @6 l/min"), rth2),
            (L("Temp. minima del fluido in ingresso", "Min. temp. of inlet fluid"), "−25 °C"),
            (L("Temp. tipica del fluido in ingresso", "Typ. temp. of inlet fluid"), "+60 °C"),
            (L("Temp. massima di funzionamento*", "Max. operating temp.*"), "+85 °C"),
        ]),
        (L("Meccaniche e ambientali", "Mechanical and environmental"), [
            (L("Forza di serraggio fino a", "Clamping force up to"), force),
            (L("Urti e vibrazioni", "Shocks and vibrations"), "IEC 77 §16"),
            (L("Portata del fluido", "Cooling flow rate"), "3 ÷ 9 l/min"),
            (L("Perdita di carico max @6 l/min", "Max. pressure drop @6 l/min"), "0,5 bar"),
            (L("Perdita di carico tipica @6 l/min", "Typ. pressure drop @6 l/min"), "0,3 bar"),
            (L("Temperatura di stoccaggio", "Storage temperature"), "−40 °C ÷ +85 °C"),
            (L("Parallelismo delle superfici", "Surface parallelism"), "0,05 mm"),
            (L("Planarità delle superfici", "Surface planarity"), "0,02 mm"),
            (L("Rugosità delle superfici", "Surface roughness"), "Ra 1,6"),
            (L("Dimensioni", "Overall dimensions"), L("vedi disegno", "see drawing")),
            (L("Peso", "Weight"), weight),
        ]),
    ]


ATLANTIS_NOTE = L(
    "* Con acqua pura; in genere dipende dal tipo di fluido e dal circuito esterno.",
    "* With pure water – usually depending on kind of cooling fluid and external circuit.",
)

# ---- prodotti -----------------------------------------------------------------
PRODUCTS = {
    "bae6": {
        "file": "atlantis-bae6.html",
        "family": "atlantis",
        "name": "ATLANTIS® BAE6",
        "subtitle": L("Raffreddatore ad acqua", "Water cooler"),
        "key": L(["Fino a 3.000 W (1.500 + 1.500)", "Area di contatto fino a Ø 49 mm", "Peso circa 160 g"],
                 ["Up to 3,000 W (1,500 + 1,500)", "Contact area up to Ø 49 mm", "Weight approx. 160 g"]),
        "power": L("che dissipano fino a 3.000 W sulle due facce (1.500 + 1.500), con un'area di contatto fino a un diametro di 49 mm (su richiesta fino a 55 mm).",
                   "dissipating up to 3.000W on both sides (1.500 + 1.500), with a contact area up to a diameter of 49mm (custom tailored up to 55mm)."),
        "text": "atlantis",
        "specs": _atlantis_specs("16 K/kW", "10,5 K/kW", "60 kN", L("160 g circa", "160 g approx.")),
        "note": ATLANTIS_NOTE,
        "images": [("atlantis-foto.jpg", L("Raffreddatori ATLANTIS", "ATLANTIS coolers")),
                   ("bae6-disegno.png", L("Disegno quotato BAE6", "BAE6 outline drawing"))],
        "thumbs": ["atlantis-foto.jpg"],
    },
    "bae9": {
        "file": "atlantis-bae9.html",
        "family": "atlantis",
        "name": "ATLANTIS® BAE9",
        "subtitle": L("Raffreddatore ad acqua", "Water cooler"),
        "key": L(["Fino a 4.000 W (2.000 + 2.000)", "Area di contatto fino a Ø 79 mm", "Peso circa 330 g"],
                 ["Up to 4,000 W (2,000 + 2,000)", "Contact area up to Ø 79 mm", "Weight approx. 330 g"]),
        "power": L("che dissipano fino a 4.000 W sulle due facce (2.000 + 2.000), con un'area di contatto fino a un diametro di 79 mm (su richiesta fino a 85 mm).",
                   "dissipating up to 4.000W on both sides (2.000 + 2.000), with a contact area up to a diameter of 79mm (custom tailored up to 85mm)."),
        "text": "atlantis",
        "specs": _atlantis_specs("11 K/kW", "7 K/kW", "90 kN", L("330 g circa", "330 g approx.")),
        "note": ATLANTIS_NOTE,
        "images": [("atlantis-foto.jpg", L("Raffreddatori ATLANTIS", "ATLANTIS coolers")),
                   ("bae9-disegno.png", L("Disegno quotato BAE9", "BAE9 outline drawing"))],
        "thumbs": ["atlantis-foto.jpg"],
    },
    "columbus1000": {
        "file": "columbus-1000.html",
        "family": "columbus",
        "name": "COLUMBUS 1000",
        "subtitle": L("Scambiatore di calore per armadi elettronici", "Heat exchanger for electronic cabinets"),
        "key": L(["100 W/K di efficienza di raffreddamento", "IP55 e NEMA 12", "Ventole 115 V/60 Hz, 220 V/50 Hz o DC 12-24-48 V"],
                 ["100 W/K cooling efficiency", "IP55 and NEMA 12", "Fans 115 V/60 Hz, 220 V/50 Hz or DC 12-24-48 V"]),
        "paragraphs": L(
            [
                "La famiglia COLUMBUS di scambiatori di calore passivi è stata progettata per armadi elettronici e camere ambientali. Ha un sistema costruttivo innovativo, estremamente leggero, e un telaio di facile montaggio.",
                "Queste unità ad alta efficienza, sviluppate sul concetto degli scambiatori controcorrente, hanno due circuiti idraulici separati, senza scambio d'aria tra armadio e ambiente.",
                "Rispettano i requisiti IP55 e NEMA 12.",
                "Possono essere montate in qualsiasi posizione, con grande flessibilità di progetto, e non richiedono manutenzione.",
                "Gli scambiatori COLUMBUS possono essere dotati di ventole standard 115 V/60 Hz o 220 V/50 Hz, oppure di ventole DC brushless (12-24-48 V), tutte con griglie di protezione.",
                "I moduli hanno un termostato tarato a 45 °C ± 5 °C e un sensore NTC per il controllo esterno della temperatura. Su richiesta sono disponibili sistemi di controllo su misura.",
                "I collegamenti elettrici sono disponibili su terminali faston standard 3×2 mm.",
                "I materiali e i componenti usati nella produzione degli scambiatori COLUMBUS di Bosari Thermal Management sono selezionati e controllati per garantire la conformità alle specifiche richieste.",
            ],
            [
                "The COLUMBUS family of passive heat exchangers has been specifically designed for electronic cabinets and environmental chambers. It features an innovative, extremely lightweight construction system, and an easy-to-mount chassis.",
                "These highly efficient units, developed upon the concept of counterflow heat exchangers, have two separated hydraulic circuits, with no air exchange between the cabinet and the ambient.",
                "They comply with IP55 and NEMA 12 requirements.",
                "They can be mounted in any position, offering a great flexibility in designing devices, and they are maintenance free.",
                "The COLUMBUS heat exchangers can be equipped with standard 115V/60Hz or 220V/50Hz fans, or with DC brushless fans (12-24-48V), all provided with finger guards.",
                "The modules feature a thermal switch set at 45°C ± 5°C and NTC sensor for external temperature control. Custom-tailored control systems are available upon demand.",
                "All the electrical connections are available on standard 3x2mm faston terminals.",
                "Materials and components used in the manufacturing of Bosari Thermal Management's COLUMBUS heat exchangers are carefully selected and quality controlled, to ensure the compliance with the requested specifications.",
            ],
        ),
        "specs": [
            (L("Caratteristiche tecniche", "Technical characteristics"), [
                (L("Efficienza di raffreddamento", "Cooling efficiency"), "100 W/K"),
                (L("Dimensioni", "Dimensions"), "440 × 1050 × 106 mm"),
                (L("Materiale cassa esterna", "External case material"), "Al 99,5%"),
                (L("Materiale nucleo scambiatore", "Exchanger core material"), L("Alluminio puro", "Pure aluminium")),
                (L("Temperatura di funzionamento", "Operating temp. range"), "−40 °C ÷ +100 °C"),
                (L("Peso", "Weight"), L("19 kg circa", "19 kg approx.")),
                (L("Ventole di ingresso", "Inlet fans"), "2 × Ø 172 mm"),
                (L("Ventole di uscita", "Outlet fans"), "2 × Ø 172 mm"),
                (L("Velocità tipica dell'aria", "Typ. air flow speed"), "3,5 m/s"),
                (L("Rumorosità tipica @3,5 m/s", "Typ. noise @3.5 m/s"), "58 dB(A)"),
                (L("Compatibilità EMC", "EMC compliances"), "EN55022 · EN50082-2 · ETS300 342-2"),
            ]),
        ],
        "note": None,
        "images": [("columbus-1.jpg", L("COLUMBUS 1000 aperto", "COLUMBUS 1000 open")),
                   ("columbus-2.jpg", L("COLUMBUS 1000, lato ventole", "COLUMBUS 1000, fan side")),
                   ("columbus-3.jpg", L("COLUMBUS 1000, retro", "COLUMBUS 1000, rear"))],
        "thumbs": ["columbus-2.jpg"],
    },
    "ucool1200": {
        "file": "u-cool-1200-50.html",
        "family": "ucool",
        "name": "U-COOL® 1200/50",
        "subtitle": L("Sistema di raffreddamento a heat pipe – Tipo 1200/50", "Heat pipe cooling system – Type 1200/50"),
        "key": L(["1.200 W a convezione naturale", "6 heat pipe a «U» in rame, 29 coppie di alette", "Peso circa 19 kg"],
                 ["1,200 W by natural convection", "6 copper “U” heat pipes, 29 couples of fins", "Weight approx. 19 kg"]),
        "sections": L(
            [
                ("Descrizione", [
                    "Questo raffreddatore a heat pipe è stato progettato per rispondere alla specifica generale preparata da un nostro cliente, relativa al raffreddamento di un inverter IGBT per applicazione su veicoli ferroviari, montato sottopavimento con le alette orientate su un piano parallelo alla direzione di marcia.",
                ]),
                ("Funzionamento", [
                    "Il calore prodotto dai moduli IGBT, montati su una piastra di base, è trasportato da 6 heat pipe a «U» fino a una sezione radiante composta da 29 coppie di alette alloggiate meccanicamente sulle heat pipe. Le alette dissipano a loro volta il calore nell'ambiente per convezione naturale dell'aria.",
                    "La forma particolare del raffreddatore garantisce anche un'efficienza molto elevata con l'aria forzata, causata dal movimento del treno (ventilazione assistita).",
                ]),
                ("Costruzione", [
                    "L'unità presentata comprende essenzialmente:",
                ]),
            ],
            [
                ("Description", [
                    "This type of Heat Pipe Cooler has been designed to meet the general specification prepared by one of our customers, regarding the cooling of an IGBT inverter for application on railway vehicles, mounted underfloor with fins oriented in a parallel plane to the moving direction.",
                ]),
                ("Operation", [
                    "The heat produced by IGBT modules, mounted on a base plate, is carried, by means of 6 “U” shaped heat pipes, to a radiating section composed by 29 couples of fins mechanically housed on the heat pipes. Fins in turn dissipate the heat into the ambient, through a natural air convection.",
                    "The particular shape of the cooler also provides a very high efficiency with the forced air, caused by the movement of the train (assisted ventilation).",
                ]),
                ("Construction", [
                    "The sample unit presented here basically consists of:",
                ]),
            ],
        ),
        "construction": L(
            [
                "Una piastra di base in lega di alluminio, lavorata su una faccia per alloggiare il tratto inferiore delle heat pipe mediante brasatura o serraggio meccanico, e sull'altra faccia per il montaggio dei moduli IGBT e dei diodi con fori filettati. Sulla stessa superficie può essere prevista una gola per alloggiare una guarnizione.",
                "Una serie di 6 heat pipe in rame, alloggiate e saldate alla piastra di base con una speciale lega per brasatura. Il fluido termovettore può essere acqua demineralizzata o fluorinert. I tubi sono inclinati di 10° rispetto all'orizzontale per consentire il funzionamento assistito dalla gravità.",
                "Una sezione dissipante formata da 29 coppie di alette in lega di alluminio, ciascuna di 420 × 135 × 1 mm. Le alette sono distanziate per favorire il flusso dell'aria di raffreddamento. Hanno sei fori ciascuna, delle dimensioni dei tubi, e sono inserite sui tubi con interferenza meccanica.",
                "Un'aletta di chiusura speciale in alluminio, spessa 3 mm, che irrigidisce la struttura dei tubi e offre un ulteriore punto di fissaggio alla struttura del treno.",
            ],
            [
                "A base plate made of Aluminum alloy, machined on one face to house the lower leg of the heat pipes by means of brazings or mechanical clamping, and on the other face to allow the mounting of IGBT modules and Diodes by means of tapped threaded holes. On this same surface a groove for housing a gasket can be provided.",
                "A series of 6 heat pipes made of Copper, housed and soldered to the base plate by means of a special soldering alloy. Thermocarrying fluid can be demineralised water or fluorinert. Pipes are inclined of 10° over the horizontal line to allow an operation mode gravity assisted.",
                "A dissipating section consisting of 29 couples of fins made of Aluminum alloy, each having dimensions of 420x135x1 mm. Fins are separated in order to provide a better flow of the cooling air. Fins have six holes each to match the pipes size and are inserted on the pipes with a mechanical interference.",
                "A special closing aluminum fin, of 3 mm thickness, is provided to ensure a stiffening of the pipes structure and an additional fixing point to the train structure.",
            ],
        ),
        "specs": [
            (L("Termiche", "Thermal"), [
                (L("Potenza termica totale", "Total thermal power"), "1200 W"),
                (L("Tipo di raffreddamento", "Type of cooling"), L("Convezione naturale dell'aria", "Natural air convection")),
                (L("Rth (base dissipatore – aria ambiente)", "Rth (heatsink baseplate – ambient air)"), "< 50 K/kW"),
            ]),
            (L("Meccaniche", "Mechanical"), [
                (L("Planarità della piastra", "Plate surface planarity"), "0,05 mm"),
                (L("Rugosità della piastra", "Plate surface roughness"), "1,2 µm"),
                (L("Finitura piastra", "Plate finish"),
                 L("Alodine bianca chimica 1000 e successiva verniciatura nera sul lato tubi",
                   "Chemical white alodine 1000 and further black painting on pipe side")),
                (L("Finitura alette", "Fins finish"), L("Verniciatura epossidica nera", "Black epoxy painting")),
                (L("Peso", "Weight"), L("19 kg circa", "19 kg approx.")),
            ]),
            (L("Ambientali", "Environmental"), [
                (L("Posizione di lavoro", "Operating position"), L("Verticale", "Vertical")),
                (L("Inclinazione ammessa", "Tilting angle"), "± 8°"),
                (L("Temperatura ambiente", "Ambient temperature range"), "−25 °C ÷ +80 °C"),
                (L("Urti e vibrazioni", "Shock and vibrations"), L("Secondo IEC 77 §16", "As per IEC 77 §16")),
            ]),
        ],
        "note": None,
        # ucool-foto.jpg = foto vera (da aggiungere); in sua assenza si usa lo schema illustrativo inventato
        "images": [("ucool-foto.jpg", L("U-COOL 1200/50", "U-COOL 1200/50")),
                   ("ucool-{lang}.svg", L("Schema illustrativo, non in scala", "Illustrative sketch, not to scale"))],
        "thumbs": ["ucool-foto.jpg", "ucool-{lang}.svg"],
    },
}
