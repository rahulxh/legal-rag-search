"""
Indian Legal Knowledge Base — sample data chunks.
Covers: Constitution of India, IPC, CrPC, fundamental rights.
Add more by uploading PDFs via the browser UI.
"""

LEGAL_DOCUMENTS = [
    # ── Constitution of India ──
    {
        "id": "const_preamble",
        "text": "The Preamble of the Constitution of India declares India to be a Sovereign, Socialist, Secular, Democratic Republic. It secures to all citizens Justice (social, economic, political), Liberty of thought, expression, belief, faith and worship, Equality of status and opportunity, and Fraternity assuring the dignity of the individual and unity of the Nation. The words 'Socialist' and 'Secular' were added by the 42nd Amendment in 1976.",
        "metadata": {"category": "constitution", "act": "Constitution of India", "language": "english"}
    },
    {
        "id": "const_art14",
        "text": "Article 14 of the Indian Constitution guarantees Equality before law. It states: The State shall not deny to any person equality before the law or the equal protection of the laws within the territory of India. This article applies to all persons including citizens and foreigners. It prohibits class legislation but permits reasonable classification.",
        "metadata": {"category": "constitution", "act": "Constitution of India", "article": "14", "language": "english"}
    },
    {
        "id": "const_art19",
        "text": "Article 19 of the Indian Constitution guarantees six fundamental freedoms to citizens: (a) freedom of speech and expression, (b) freedom to assemble peaceably without arms, (c) freedom to form associations or unions, (d) freedom to move freely throughout India, (e) freedom to reside and settle in any part of India, (g) freedom to practise any profession or carry on any occupation, trade or business. These rights are subject to reasonable restrictions by the State.",
        "metadata": {"category": "constitution", "act": "Constitution of India", "article": "19", "language": "english"}
    },
    {
        "id": "const_art21",
        "text": "Article 21 of the Indian Constitution states: No person shall be deprived of his life or personal liberty except according to procedure established by law. The Supreme Court has given a very wide interpretation to Article 21. It includes right to live with dignity, right to privacy, right to education, right to health, right to a clean environment, right to speedy trial, and right to legal aid.",
        "metadata": {"category": "constitution", "act": "Constitution of India", "article": "21", "language": "english"}
    },
    {
        "id": "const_art32",
        "text": "Article 32 is called the 'Heart and Soul of the Constitution' by Dr. B.R. Ambedkar. It gives the right to move the Supreme Court for enforcement of Fundamental Rights. The Supreme Court can issue five types of writs: Habeas Corpus (to produce the body), Mandamus (to perform duty), Prohibition (to lower courts), Certiorari (to quash orders), and Quo Warranto (to challenge authority).",
        "metadata": {"category": "constitution", "act": "Constitution of India", "article": "32", "language": "english"}
    },
    {
        "id": "const_dpsp",
        "text": "Directive Principles of State Policy (DPSP) are contained in Part IV (Articles 36-51) of the Indian Constitution. They are non-justiciable, meaning they cannot be enforced by courts. However, they are fundamental in the governance of the country. Key DPSPs include: equal pay for equal work (Article 39d), right to work (Article 41), free and compulsory education for children (Article 45), living wage for workers (Article 43), and uniform civil code (Article 44).",
        "metadata": {"category": "constitution", "act": "Constitution of India", "part": "IV", "language": "english"}
    },
    {
        "id": "const_amendment",
        "text": "Article 368 of the Indian Constitution deals with the power of Parliament to amend the Constitution. There are three types of amendments: (1) Simple majority — ordinary bills passed by Parliament, (2) Special majority — two-thirds majority of members present and voting, and (3) Special majority plus ratification by at least half the State Legislatures — for federal provisions. The Basic Structure doctrine established in Kesavananda Bharati case (1973) limits amendment power.",
        "metadata": {"category": "constitution", "act": "Constitution of India", "article": "368", "language": "english"}
    },

    # ── IPC (Indian Penal Code) ──
    {
        "id": "ipc_overview",
        "text": "The Indian Penal Code (IPC) 1860 is the official criminal code of India. It was drafted by the First Law Commission of India under Thomas Babington Macaulay. The IPC covers all substantive aspects of criminal law and applies to the whole of India. It has 511 sections divided into 23 chapters. It defines various offences and their punishments. The IPC has been replaced by the Bharatiya Nyaya Sanhita (BNS) 2023 which came into force on 1 July 2024.",
        "metadata": {"category": "criminal_law", "act": "IPC", "language": "english"}
    },
    {
        "id": "ipc_sec302",
        "text": "Section 302 of the Indian Penal Code deals with Punishment for Murder. It states: Whoever commits murder shall be punished with death, or imprisonment for life, and shall also be liable to fine. Murder is defined under Section 300 IPC as culpable homicide with the intention to cause death, or with the intention to cause such bodily injury as the offender knows to be likely to cause death, or with the intention of causing bodily injury sufficient in the ordinary course of nature to cause death.",
        "metadata": {"category": "criminal_law", "act": "IPC", "section": "302", "language": "english"}
    },
    {
        "id": "ipc_sec420",
        "text": "Section 420 of the Indian Penal Code deals with Cheating and dishonestly inducing delivery of property. Whoever cheats and thereby dishonestly induces the person deceived to deliver any property to any person, or to make, alter or destroy the whole or any part of a valuable security, shall be punished with imprisonment of either description for a term which may extend to seven years, and shall also be liable to fine. This is a cognizable and non-bailable offence.",
        "metadata": {"category": "criminal_law", "act": "IPC", "section": "420", "language": "english"}
    },
    {
        "id": "ipc_sec375",
        "text": "Section 375 of the Indian Penal Code defines Rape. A man is said to commit rape if he penetrates the vagina, mouth, urethra or anus of a woman without her consent, or with her consent obtained by force, fraud, or misrepresentation. The punishment under Section 376 IPC is rigorous imprisonment of not less than 10 years, which may extend to life imprisonment, along with fine. The Criminal Law Amendment Act 2013 (Nirbhaya Act) significantly strengthened these provisions.",
        "metadata": {"category": "criminal_law", "act": "IPC", "section": "375", "language": "english"}
    },
    {
        "id": "ipc_sec499",
        "text": "Section 499 of the Indian Penal Code defines Defamation. Whoever, by words either spoken or intended to be read, or by signs or by visible representations, makes or publishes any imputation concerning any person intending to harm, or knowing or having reason to believe that such imputation will harm, the reputation of such person, is said to defame that person. Section 500 provides punishment of simple imprisonment up to two years, or fine, or both. There are ten exceptions to defamation under IPC.",
        "metadata": {"category": "criminal_law", "act": "IPC", "section": "499", "language": "english"}
    },

    # ── CrPC (Code of Criminal Procedure) ──
    {
        "id": "crpc_overview",
        "text": "The Code of Criminal Procedure (CrPC) 1973 is the main legislation for procedure for administration of substantive criminal law in India. It provides the machinery for detection of crime, apprehension of suspects, collection of evidence, determination of guilt or innocence of the accused and determination of punishment. The CrPC has 484 sections. It has been replaced by Bharatiya Nagarik Suraksha Sanhita (BNSS) 2023 effective from 1 July 2024.",
        "metadata": {"category": "criminal_procedure", "act": "CrPC", "language": "english"}
    },
    {
        "id": "crpc_bail",
        "text": "Bail under CrPC: Bailable offences are those where bail is a matter of right (Section 436 CrPC). Non-bailable offences require court discretion for bail (Section 437 CrPC). Anticipatory bail (Section 438 CrPC) can be granted by Sessions Court or High Court before arrest. The Supreme Court in Arnesh Kumar vs State of Bihar (2014) held that arrest should not be made mechanically in cases punishable with less than 7 years imprisonment.",
        "metadata": {"category": "criminal_procedure", "act": "CrPC", "topic": "bail", "language": "english"}
    },
    {
        "id": "crpc_fir",
        "text": "FIR (First Information Report) under Section 154 CrPC: Any person can give information of a cognizable offence to the police officer in charge of a police station. The officer must register the FIR and give a copy to the informant free of cost. If the officer refuses to register FIR, the person can send information in writing to the Superintendent of Police. The Supreme Court in Lalita Kumari case (2014) held that registration of FIR is mandatory for cognizable offences.",
        "metadata": {"category": "criminal_procedure", "act": "CrPC", "section": "154", "topic": "FIR", "language": "english"}
    },

    # ── Hindi entries ──
    {
        "id": "hindi_art21",
        "text": "अनुच्छेद 21 भारतीय संविधान का सबसे महत्वपूर्ण अनुच्छेद है। इसमें लिखा है: किसी व्यक्ति को उसके प्राण या दैहिक स्वतंत्रता से विधि द्वारा स्थापित प्रक्रिया के अनुसार ही वंचित किया जाएगा, अन्यथा नहीं। सर्वोच्च न्यायालय ने इसकी व्याख्या बहुत व्यापक रूप से की है। इसमें गरिमा के साथ जीने का अधिकार, निजता का अधिकार, स्वास्थ्य का अधिकार, शिक्षा का अधिकार और त्वरित सुनवाई का अधिकार शामिल हैं।",
        "metadata": {"category": "constitution", "act": "Constitution of India", "article": "21", "language": "hindi"}
    },
    {
        "id": "hindi_ipc302",
        "text": "भारतीय दंड संहिता की धारा 302 हत्या के लिए दंड का प्रावधान करती है। इस धारा के अनुसार जो कोई हत्या करेगा वह मृत्युदंड या आजीवन कारावास से दंडित किया जाएगा और जुर्माने के लिए भी उत्तरदायी होगा। धारा 300 के अंतर्गत हत्या को परिभाषित किया गया है। हत्या और गैर-इरादतन हत्या (culpable homicide not amounting to murder) में मुख्य अंतर इरादे का होता है।",
        "metadata": {"category": "criminal_law", "act": "IPC", "section": "302", "language": "hindi"}
    },
    {
        "id": "hindi_fir",
        "text": "प्रथम सूचना रिपोर्ट (FIR) दंड प्रक्रिया संहिता की धारा 154 के अंतर्गत दर्ज की जाती है। कोई भी व्यक्ति संज्ञेय अपराध की जानकारी पुलिस थाने के प्रभारी अधिकारी को दे सकता है। अधिकारी FIR दर्ज करने के लिए बाध्य है और शिकायतकर्ता को निःशुल्क प्रति देनी होगी। यदि पुलिस FIR दर्ज करने से मना करती है तो पुलिस अधीक्षक को लिखित सूचना दी जा सकती है। सर्वोच्च न्यायालय ने ललिता कुमारी मामले में कहा कि संज्ञेय अपराध में FIR दर्ज करना अनिवार्य है।",
        "metadata": {"category": "criminal_procedure", "act": "CrPC", "section": "154", "language": "hindi"}
    },

    # ── Malayalam entries ──
    {
        "id": "mal_art21",
        "text": "ഭാരതീയ ഭരണഘടനയുടെ ആർട്ടിക്കിൾ 21 ജീവിക്കാനുള്ള അവകാശവും വ്യക്തി സ്വാതന്ത്ര്യവും ഉറപ്പ് നൽകുന്നു. നിയമം നിശ്ചയിച്ചിട്ടുള്ള നടപടിക്രമം അനുസരിച്ചല്ലാതെ ഒരു വ്യക്തിയുടെ ജീവനോ വ്യക്തിസ്വാതന്ത്ര്യമോ ഇല്ലാതാക്കാൻ പാടുള്ളതല്ല. സുപ്രീം കോടതി ഈ ആർട്ടിക്കിളിന് വളരെ വ്യാപകമായ വ്യാഖ്യാനം നൽകിയിട്ടുണ്ട്. അന്തസ്സോടെ ജീവിക്കാനുള്ള അവകാശം, സ്വകാര്യതയ്ക്കുള്ള അവകാശം, ആരോഗ്യത്തിനുള്ള അവകാശം എന്നിവ ഇതിൽ ഉൾപ്പെടുന്നു.",
        "metadata": {"category": "constitution", "act": "Constitution of India", "article": "21", "language": "malayalam"}
    },
    {
        "id": "mal_fundamental_rights",
        "text": "ഭാരതീയ ഭരണഘടനയുടെ മൂന്നാം ഭാഗത്തിൽ (ആർട്ടിക്കിൾ 12-35) മൗലികാവകാശങ്ങൾ പ്രതിപാദിക്കുന്നു. ആറ് മൗലികാവകാശങ്ങൾ: (1) സമത്വത്തിനുള്ള അവകാശം (Art 14-18), (2) സ്വാതന്ത്ര്യത്തിനുള്ള അവകാശം (Art 19-22), (3) ചൂഷണത്തിനെതിരായ അവകാശം (Art 23-24), (4) മതസ്വാതന്ത്ര്യത്തിനുള്ള അവകാശം (Art 25-28), (5) സാംസ്കാരിക-വിദ്യാഭ്യാസ അവകാശം (Art 29-30), (6) ഭരണഘടനാ പരിഹാരത്തിനുള്ള അവകാശം (Art 32).",
        "metadata": {"category": "constitution", "act": "Constitution of India", "language": "malayalam"}
    },

    # ── Consumer Protection ──
    {
        "id": "consumer_act",
        "text": "The Consumer Protection Act 2019 replaced the 1986 Act. It provides for protection of interests of consumers. Key features: establishment of Central Consumer Protection Authority (CCPA), e-commerce regulations, product liability, unfair trade practices. Consumers can file complaints in District Commission (up to Rs 1 crore), State Commission (Rs 1-10 crore), or National Commission (above Rs 10 crore). The Act provides for mediation as an alternative dispute resolution mechanism.",
        "metadata": {"category": "civil_law", "act": "Consumer Protection Act 2019", "language": "english"}
    },

    # ── RTI ──
    {
        "id": "rti_act",
        "text": "The Right to Information Act 2005 (RTI) empowers citizens to request information from public authorities. Key provisions: Section 6 — any citizen can file RTI application with Rs 10 fee; Section 7 — information must be provided within 30 days (48 hours if life/liberty is involved); Section 8 — exemptions from disclosure (national security, personal information etc.); Section 19 — first appeal to senior officer, second appeal to State/Central Information Commission. RTI does not apply to intelligence agencies like IB, RAW.",
        "metadata": {"category": "civil_law", "act": "RTI Act 2005", "language": "english"}
    },
]
