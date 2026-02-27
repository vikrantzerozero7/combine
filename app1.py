import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(layout="wide")

# ============================================
# LANGUAGE CONFIGURATION
# ============================================
LANGUAGES = {
    "english": "English",
    "hindi": "हिंदी"
}

# ============================================
# CHEMISTRY CONFIGURATION - WITH BOTH CHAPTERS
# ============================================

CHEMISTRY_CONFIG = {
    "title": {
        "english": "CHEMISTRY12",
        "hindi": "रसायन विज्ञान"
    },
    "chapters": [
        # ============================================
        # CHAPTER 1: SOLUTIONS
        # ============================================
        {
            "id": "chapter1",
            "display_name": {
                "english": "CHAPTER 1: SOLUTIONS",
                "hindi": "अध्याय 1: विलयन"
            },
            "color": "#FF9933",
            "topics": [
                {
                    "id": "topic1_1",
                    "display_name": {
                        "english": "EXPRESSING CONCENTRATION",
                        "hindi": "सांद्रता को व्यक्त करना"
                    },
                    "article_range": "Section 1.2",
                    "concepts": [
                        {
                            "id": "concept1_1_1",
                            "display_name": {
                                "english": "Mass Percentage (w/w)",
                                "hindi": "द्रव्यमान प्रतिशत (w/w)"
                            },
                            "description": {
                                "english": "Mass % of component = (Mass of component / Total mass of solution) × 100",
                                "hindi": "किसी घटक का द्रव्यमान % = (घटक का द्रव्यमान / विलयन का कुल द्रव्यमान) × 100"
                            }
                        },
                        {
                            "id": "concept1_1_2",
                            "display_name": {
                                "english": "Volume Percentage (v/v)",
                                "hindi": "आयतन प्रतिशत (v/v)"
                            },
                            "description": {
                                "english": "Volume % = (Volume of component / Total volume of solution) × 100\nCommon for liquid-liquid solutions (e.g., 10% ethanol in water).",
                                "hindi": "आयतन % = (घटक का आयतन / विलयन का कुल आयतन) × 100\nद्रव-द्रव विलयनों के लिए सामान्य (जैसे, जल में 10% एथेनॉल)।"
                            }
                        },
                        {
                            "id": "concept1_1_3",
                            "display_name": {
                                "english": "Parts per Million (ppm)",
                                "hindi": "पार्ट्स पर मिलियन (ppm)"
                            },
                            "description": {
                                "english": "ppm = (Number of parts of component / Total parts of all components) × 10⁶\nUsed for trace concentrations (pollutants in water/air).",
                                "hindi": "ppm = (घटक के भागों की संख्या / सभी घटकों के कुल भाग) × 10⁶\nअल्प मात्रा सांद्रता के लिए प्रयुक्त (जल/वायु में प्रदूषक)।"
                            }
                        },
                        {
                            "id": "concept1_1_4",
                            "display_name": {
                                "english": "Mole Fraction (x)",
                                "hindi": "मोल प्रभाज (x)"
                            },
                            "description": {
                                "english": "x_A = n_A / (n_A + n_B + ...)\nSum of mole fractions of all components = 1.\nDimensionless, independent of temperature.",
                                "hindi": "x_A = n_A / (n_A + n_B + ...)\nसभी घटकों के मोल प्रभाजों का योग = 1.\nविमाहीन, तापमान से स्वतंत्र।"
                            }
                        },
                        {
                            "id": "concept1_1_5",
                            "display_name": {
                                "english": "Molarity (M)",
                                "hindi": "मोलरिटी (M)"
                            },
                            "description": {
                                "english": "M = moles of solute / Volume of solution in litres\nUnit: mol/L or M.\nDepends on temperature (volume changes with T).",
                                "hindi": "M = विलेय के मोल / विलयन का आयतन लीटर में\nमात्रक: mol/L या M.\nतापमान पर निर्भर करता है (आयतन ताप के साथ बदलता है)।"
                            }
                        },
                        {
                            "id": "concept1_1_6",
                            "display_name": {
                                "english": "Molality (m)",
                                "hindi": "मोललिटी (m)"
                            },
                            "description": {
                                "english": "m = moles of solute / Mass of solvent in kg\nUnit: mol/kg.\nIndependent of temperature (mass is constant).",
                                "hindi": "m = विलेय के मोल / विलायक का द्रव्यमान kg में\nमात्रक: mol/kg.\nतापमान से स्वतंत्र (द्रव्यमान स्थिर रहता है)।"
                            }
                        }
                    ]
                },
                {
                    "id": "topic1_2",
                    "display_name": {
                        "english": "SOLUBILITY",
                        "hindi": "विलेयता"
                    },
                    "article_range": "Section 1.3",
                    "concepts": [
                        {
                            "id": "concept1_2_1",
                            "display_name": {
                                "english": "Solubility of Solids in Liquids",
                                "hindi": "द्रवों में ठोसों की विलेयता"
                            },
                            "description": {
                                "english": "• Like dissolves like: Polar solutes dissolve in polar solvents, non-polar in non-polar.\n• Dynamic equilibrium: Solute + Solvent ⇌ Solution.\n• Saturated solution contains maximum solute at given T and P.\n• Effect of T: If dissolution is endothermic, solubility increases with T; if exothermic, it decreases.",
                                "hindi": "• समान समान में घुलता है: ध्रुवीय विलेय ध्रुवीय विलायकों में घुलते हैं, अध्रुवीय अध्रुवीय में।\n• गतिक साम्य: विलेय + विलायक ⇌ विलयन.\n• संतृप्त विलयन में दिए गए T और P पर अधिकतम विलेय होता है।\n• T का प्रभाव: यदि विलयन ऊष्माशोषी है, ताप बढ़ने पर विलेयता बढ़ती है; यदि ऊष्माक्षेपी है, तो घटती है।"
                            }
                        },
                        {
                            "id": "concept1_2_2",
                            "display_name": {
                                "english": "Henry's Law (Gas Solubility)",
                                "hindi": "हेनरी का नियम (गैस की विलेयता)"
                            },
                            "description": {
                                "english": "p = K_H × x\np = partial pressure of gas, x = mole fraction of gas in solution, K_H = Henry's constant.\nHigher K_H means lower solubility.\nApplications: Soft drinks (high CO₂ pressure), scuba diving (air diluted with He to avoid 'bends'), high altitude anoxia.",
                                "hindi": "p = K_H × x\np = गैस का आंशिक दाब, x = विलयन में गैस का मोल प्रभाज, K_H = हेनरी स्थिरांक।\nअधिक K_H का अर्थ कम विलेयता।\nअनुप्रयोग: शीतल पेय (उच्च CO₂ दाब), स्कूबा डाइविंग (bends से बचने के लिए He मिश्रण), उच्च ऊंचाई पर एनोक्सिया।"
                            }
                        },
                        {
                            "id": "concept1_2_3",
                            "display_name": {
                                "english": "Effect of Temperature and Pressure on Gas Solubility",
                                "hindi": "गैस की विलेयता पर ताप और दाब का प्रभाव"
                            },
                            "description": {
                                "english": "• Solubility of gases decreases with increase in temperature (dissolution is exothermic).\n• Solubility increases with increase in partial pressure (Henry's Law).",
                                "hindi": "• तापमान बढ़ने पर गैसों की विलेयता घटती है (विलयन ऊष्माक्षेपी है)।\n• आंशिक दाब बढ़ने पर विलेयता बढ़ती है (हेनरी का नियम)।"
                            }
                        }
                    ]
                },
                {
                    "id": "topic1_3",
                    "display_name": {
                        "english": "VAPOUR PRESSURE OF LIQUID SOLUTIONS",
                        "hindi": "द्रव विलयनों का वाष्प दाब"
                    },
                    "article_range": "Section 1.4",
                    "concepts": [
                        {
                            "id": "concept1_3_1",
                            "display_name": {
                                "english": "Raoult's Law (Volatile Liquids)",
                                "hindi": "राउल्ट का नियम (वाष्पशील द्रव)"
                            },
                            "description": {
                                "english": "For a solution of two volatile liquids:\np₁ = x₁p₁⁰, p₂ = x₂p₂⁰\np_total = p₁ + p₂ = x₁p₁⁰ + x₂p₂⁰ = p₂⁰ + (p₁⁰ - p₂⁰)x₁\nVapour phase composition: y₁ = p₁/p_total",
                                "hindi": "दो वाष्पशील द्रवों के विलयन के लिए:\np₁ = x₁p₁⁰, p₂ = x₂p₂⁰\np_total = p₁ + p₂ = x₁p₁⁰ + x₂p₂⁰ = p₂⁰ + (p₁⁰ - p₂⁰)x₁\nवाष्प अवस्था संघटन: y₁ = p₁/p_total"
                            }
                        },
                        {
                            "id": "concept1_3_2",
                            "display_name": {
                                "english": "Raoult's Law (Non-Volatile Solute)",
                                "hindi": "राउल्ट का नियम (अवाष्पशील विलेय)"
                            },
                            "description": {
                                "english": "For a solution of a non-volatile solute in a volatile solvent:\np₁ = x₁p₁⁰\nLowering of vapour pressure: Δp = p₁⁰ - p₁ = p₁⁰x₂\nRelative lowering: Δp/p₁⁰ = x₂",
                                "hindi": "वाष्पशील विलायक में अवाष्पशील विलेय के विलयन के लिए:\np₁ = x₁p₁⁰\nवाष्प दाब का अवनमन: Δp = p₁⁰ - p₁ = p₁⁰x₂\nआपेक्षिक अवनमन: Δp/p₁⁰ = x₂"
                            }
                        }
                    ]
                },
                {
                    "id": "topic1_4",
                    "display_name": {
                        "english": "IDEAL AND NON-IDEAL SOLUTIONS",
                        "hindi": "आदर्श एवं अनादर्श विलयन"
                    },
                    "article_range": "Section 1.5",
                    "concepts": [
                        {
                            "id": "concept1_4_1",
                            "display_name": {
                                "english": "Ideal Solutions",
                                "hindi": "आदर्श विलयन"
                            },
                            "description": {
                                "english": "Obey Raoult's law at all concentrations.\nΔmixH = 0, ΔmixV = 0.\nA-A and B-B interactions are similar to A-B.\nExamples: n-hexane + n-heptane, benzene + toluene.",
                                "hindi": "सभी सांद्रताओं पर राउल्ट के नियम का पालन करते हैं।\nΔमिश्रणH = 0, Δमिश्रणV = 0.\nA-A और B-B अन्योन्य क्रियाएं, A-B के समान होती हैं।\nउदाहरण: n-हेक्सेन + n-हेप्टेन, बेंजीन + टॉलूईन।"
                            }
                        },
                        {
                            "id": "concept1_4_2",
                            "display_name": {
                                "english": "Non-Ideal Solutions (Positive Deviation)",
                                "hindi": "अनादर्श विलयन (धनात्मक विचलन)"
                            },
                            "description": {
                                "english": "p_total > p_total(ideal).\nΔmixH > 0, ΔmixV > 0.\nA-B interactions are weaker than A-A and B-B.\nExample: ethanol + acetone, ethanol + water.\nForms minimum boiling azeotropes.",
                                "hindi": "p_total > p_total(आदर्श).\nΔमिश्रणH > 0, Δमिश्रणV > 0.\nA-B अन्योन्य क्रियाएं, A-A और B-B से दुर्बल होती हैं।\nउदाहरण: एथेनॉल + एसीटोन, एथेनॉल + जल।\nन्यूनतम क्वथनांकी एजियोट्रोप बनाते हैं।"
                            }
                        },
                        {
                            "id": "concept1_4_3",
                            "display_name": {
                                "english": "Non-Ideal Solutions (Negative Deviation)",
                                "hindi": "अनादर्श विलयन (ऋणात्मक विचलन)"
                            },
                            "description": {
                                "english": "p_total < p_total(ideal).\nΔmixH < 0, ΔmixV < 0.\nA-B interactions are stronger than A-A and B-B.\nExample: HNO₃ + water, chloroform + acetone.\nForms maximum boiling azeotropes.",
                                "hindi": "p_total < p_total(आदर्श).\nΔमिश्रणH < 0, Δमिश्रणV < 0.\nA-B अन्योन्य क्रियाएं, A-A और B-B से प्रबल होती हैं।\nउदाहरण: HNO₃ + जल, क्लोरोफॉर्म + एसीटोन।\nअधिकतम क्वथनांकी एजियोट्रोप बनाते हैं।"
                            }
                        }
                    ]
                },
                {
                    "id": "topic1_5",
                    "display_name": {
                        "english": "COLLIGATIVE PROPERTIES",
                        "hindi": "अणुसंख्यक गुणधर्म"
                    },
                    "article_range": "Section 1.6",
                    "concepts": [
                        {
                            "id": "concept1_5_1",
                            "display_name": {
                                "english": "Relative Lowering of Vapour Pressure",
                                "hindi": "वाष्प दाब का आपेक्षिक अवनमन"
                            },
                            "description": {
                                "english": "Δp₁/p₁⁰ = x₂\nFor molar mass determination:\n(p₁⁰ - p)/p₁⁰ = (w₂/M₂) / (w₁/M₁)  (for dilute solutions)",
                                "hindi": "Δp₁/p₁⁰ = x₂\nमोलर द्रव्यमान निर्धारण हेतु:\n(p₁⁰ - p)/p₁⁰ = (w₂/M₂) / (w₁/M₁) (तनु विलयनों के लिए)"
                            }
                        },
                        {
                            "id": "concept1_5_2",
                            "display_name": {
                                "english": "Elevation of Boiling Point (ΔTb)",
                                "hindi": "क्वथनांक में उन्नयन (ΔTb)"
                            },
                            "description": {
                                "english": "ΔTb = Kb × m\nKb = ebullioscopic constant.\nM₂ = (1000 × w₂ × Kb) / (ΔTb × w₁)",
                                "hindi": "ΔTb = Kb × m\nKb = क्वथनांकी स्थिरांक।\nM₂ = (1000 × w₂ × Kb) / (ΔTb × w₁)"
                            }
                        },
                        {
                            "id": "concept1_5_3",
                            "display_name": {
                                "english": "Depression of Freezing Point (ΔTf)",
                                "hindi": "हिमांक में अवनमन (ΔTf)"
                            },
                            "description": {
                                "english": "ΔTf = Kf × m\nKf = cryoscopic constant.\nM₂ = (1000 × w₂ × Kf) / (ΔTf × w₁)",
                                "hindi": "ΔTf = Kf × m\nKf = हिमांकी स्थिरांक।\nM₂ = (1000 × w₂ × Kf) / (ΔTf × w₁)"
                            }
                        },
                        {
                            "id": "concept1_5_4",
                            "display_name": {
                                "english": "Osmosis and Osmotic Pressure (Π)",
                                "hindi": "परासरण एवं परासरण दाब (Π)"
                            },
                            "description": {
                                "english": "Π = CRT = (n₂/V)RT\nFor molar mass: M₂ = (w₂RT) / (ΠV)\nIsotonic solutions have same Π.\nHypertonic solution causes cell to shrink; hypotonic causes swelling.",
                                "hindi": "Π = CRT = (n₂/V)RT\nमोलर द्रव्यमान हेतु: M₂ = (w₂RT) / (ΠV)\nसमपरासरी विलयनों का Π समान होता है।\nअतिपरासरी विलयन कोशिका को संकुचित करता है; अल्पपरासरी सूजन पैदा करता है।"
                            }
                        },
                        {
                            "id": "concept1_5_5",
                            "display_name": {
                                "english": "Reverse Osmosis",
                                "hindi": "विपरीत परासरण"
                            },
                            "description": {
                                "english": "If pressure > Π is applied on solution side, solvent flows from solution to pure solvent.\nUsed in desalination of sea water.",
                                "hindi": "यदि विलयन पक्ष पर Π से अधिक दाब लगाया जाए, विलायक विलयन से शुद्ध विलायक की ओर प्रवाहित होता है।\nसमुद्री जल के अलवणीकरण में प्रयुक्त।"
                            }
                        }
                    ]
                },
                {
                    "id": "topic1_6",
                    "display_name": {
                        "english": "ABNORMAL MOLAR MASSES",
                        "hindi": "असामान्य मोलर द्रव्यमान"
                    },
                    "article_range": "Section 1.7",
                    "concepts": [
                        {
                            "id": "concept1_6_1",
                            "display_name": {
                                "english": "van't Hoff Factor (i)",
                                "hindi": "वांट हॉफ गुणांक (i)"
                            },
                            "description": {
                                "english": "i = Normal molar mass / Abnormal molar mass = Observed colligative property / Calculated colligative property.\ni > 1 for dissociation, i < 1 for association.",
                                "hindi": "i = सामान्य मोलर द्रव्यमान / असामान्य मोलर द्रव्यमान = प्रेक्षित अणुसंख्यक गुण / परिकलित अणुसंख्यक गुण।\nवियोजन के लिए i > 1, संगुणन के लिए i < 1."
                            }
                        },
                        {
                            "id": "concept1_6_2",
                            "display_name": {
                                "english": "Modified Colligative Property Equations",
                                "hindi": "संशोधित अणुसंख्यक गुणधर्म समीकरण"
                            },
                            "description": {
                                "english": "Δp/p₁⁰ = i(n₂/n₁) (approx.)\nΔTb = i Kb m\nΔTf = i Kf m\nΠ = i n₂ RT / V",
                                "hindi": "Δp/p₁⁰ = i(n₂/n₁) (लगभग)\nΔTb = i Kb m\nΔTf = i Kf m\nΠ = i n₂ RT / V"
                            }
                        },
                        {
                            "id": "concept1_6_3",
                            "display_name": {
                                "english": "Dissociation and Association Examples",
                                "hindi": "वियोजन एवं संगुणन के उदाहरण"
                            },
                            "description": {
                                "english": "• Dissociation: KCl → K⁺ + Cl⁻, i ≈ 2.\n• Association: 2CH₃COOH ⇌ (CH₃COOH)₂ in benzene, i ≈ 0.5.",
                                "hindi": "• वियोजन: KCl → K⁺ + Cl⁻, i ≈ 2.\n• संगुणन: 2CH₃COOH ⇌ (CH₃COOH)₂ बेंजीन में, i ≈ 0.5."
                            }
                        }
                    ]
                }
            ]
        },
        # ============================================
        # CHAPTER 2: ELECTROCHEMISTRY
        # ============================================
        {
            "id": "chapter2",
            "display_name": {
                "english": "CHAPTER 2: ELECTROCHEMISTRY",
                "hindi": "अध्याय 2: वैद्युत रसायन"
            },
            "color": "#0066CC",
            "topics": [
                {
                    "id": "topic2_1",
                    "display_name": {
                        "english": "ELECTROCHEMICAL CELLS",
                        "hindi": "वैद्युत रासायनिक सेल"
                    },
                    "article_range": "Sections 2.1-2.2",
                    "concepts": [
                        {
                            "id": "concept2_1_1",
                            "display_name": {
                                "english": "Galvanic Cell",
                                "hindi": "गैल्वेनी सेल"
                            },
                            "description": {
                                "english": "Converts chemical energy of spontaneous redox reaction into electrical energy.\nExample: Daniell Cell: Zn(s) | Zn²⁺(aq) || Cu²⁺(aq) | Cu(s).\nAnode (oxidation): Zn → Zn²⁺ + 2e⁻\nCathode (reduction): Cu²⁺ + 2e⁻ → Cu",
                                "hindi": "स्वतः प्रवर्तित रेडॉक्स अभिक्रिया की रासायनिक ऊर्जा को विद्युत ऊर्जा में बदलता है।\nउदाहरण: डेनियल सेल: Zn(s) | Zn²⁺(aq) || Cu²⁺(aq) | Cu(s).\nएनोड (ऑक्सीकरण): Zn → Zn²⁺ + 2e⁻\nकैथोड (अपचयन): Cu²⁺ + 2e⁻ → Cu"
                            }
                        },
                        {
                            "id": "concept2_1_2",
                            "display_name": {
                                "english": "Standard Electrode Potential (E⁰)",
                                "hindi": "मानक इलेक्ट्रोड विभव (E⁰)"
                            },
                            "description": {
                                "english": "Measured against Standard Hydrogen Electrode (SHE) assigned E⁰ = 0.00 V.\nSHE: Pt(s) | H₂(g, 1 bar) | H⁺(aq, 1 M).\nE⁰_cell = E⁰_cathode - E⁰_anode.",
                                "hindi": "मानक हाइड्रोजन इलेक्ट्रोड (SHE) के सापेक्ष मापा जाता है जिसका E⁰ = 0.00 V होता है।\nSHE: Pt(s) | H₂(g, 1 bar) | H⁺(aq, 1 M).\nE⁰_सेल = E⁰_कैथोड - E⁰_एनोड."
                            }
                        }
                    ]
                },
                {
                    "id": "topic2_2",
                    "display_name": {
                        "english": "NERST EQUATION",
                        "hindi": "नर्नस्ट समीकरण"
                    },
                    "article_range": "Section 2.3",
                    "concepts": [
                        {
                            "id": "concept2_2_1",
                            "display_name": {
                                "english": "Nernst Equation for Electrode",
                                "hindi": "इलेक्ट्रोड के लिए नर्नस्ट समीकरण"
                            },
                            "description": {
                                "english": "For Mⁿ⁺(aq) + ne⁻ → M(s):\nE_(Mⁿ⁺/M) = E⁰_(Mⁿ⁺/M) - (RT/nF) ln(1/[Mⁿ⁺])\nAt 298K: E = E⁰ - (0.059/n) log(1/[Mⁿ⁺])",
                                "hindi": "Mⁿ⁺(aq) + ne⁻ → M(s) के लिए:\nE_(Mⁿ⁺/M) = E⁰_(Mⁿ⁺/M) - (RT/nF) ln(1/[Mⁿ⁺])\n298K पर: E = E⁰ - (0.059/n) log(1/[Mⁿ⁺])"
                            }
                        },
                        {
                            "id": "concept2_2_2",
                            "display_name": {
                                "english": "Nernst Equation for Cell",
                                "hindi": "सेल के लिए नर्नस्ट समीकरण"
                            },
                            "description": {
                                "english": "E_cell = E⁰_cell - (RT/nF) ln Q\nFor Daniell cell at 298K: E_cell = 1.1 - (0.059/2) log([Zn²⁺]/[Cu²⁺])",
                                "hindi": "E_सेल = E⁰_सेल - (RT/nF) ln Q\nडेनियल सेल के लिए 298K पर: E_सेल = 1.1 - (0.059/2) log([Zn²⁺]/[Cu²⁺])"
                            }
                        },
                        {
                            "id": "concept2_2_3",
                            "display_name": {
                                "english": "Equilibrium Constant from Nernst Equation",
                                "hindi": "नर्नस्ट समीकरण से साम्य स्थिरांक"
                            },
                            "description": {
                                "english": "At equilibrium, E_cell = 0.\nlog Kc = (n E⁰_cell) / (0.059)  (at 298K)",
                                "hindi": "साम्यावस्था पर, E_सेल = 0.\nlog Kc = (n E⁰_सेल) / (0.059) (298K पर)"
                            }
                        }
                    ]
                },
                {
                    "id": "topic2_3",
                    "display_name": {
                        "english": "GIBBS ENERGY AND CELL POTENTIAL",
                        "hindi": "गिब्स ऊर्जा एवं सेल विभव"
                    },
                    "article_range": "Section 2.3.2",
                    "concepts": [
                        {
                            "id": "concept2_3_1",
                            "display_name": {
                                "english": "Relation between ΔG and E_cell",
                                "hindi": "ΔG और E_सेल में संबंध"
                            },
                            "description": {
                                "english": "ΔrG = -nFE_cell\nΔrG⁰ = -nFE⁰_cell\nΔrG⁰ = -RT ln Kc",
                                "hindi": "ΔrG = -nFE_सेल\nΔrG⁰ = -nFE⁰_सेल\nΔrG⁰ = -RT ln Kc"
                            }
                        }
                    ]
                },
                {
                    "id": "topic2_4",
                    "display_name": {
                        "english": "CONDUCTANCE OF ELECTROLYTIC SOLUTIONS",
                        "hindi": "वैद्युत अपघट्यों के विलयनों का चालकत्व"
                    },
                    "article_range": "Section 2.4",
                    "concepts": [
                        {
                            "id": "concept2_4_1",
                            "display_name": {
                                "english": "Resistivity (ρ) and Conductivity (κ)",
                                "hindi": "प्रतिरोधकता (ρ) एवं चालकता (κ)"
                            },
                            "description": {
                                "english": "R = ρ (l/A)\nκ = 1/ρ\nUnits: κ in S m⁻¹ or S cm⁻¹.\nConductivity decreases with dilution.",
                                "hindi": "R = ρ (l/A)\nκ = 1/ρ\nमात्रक: κ का S m⁻¹ या S cm⁻¹ में।\nतनुता के साथ चालकता घटती है।"
                            }
                        },
                        {
                            "id": "concept2_4_2",
                            "display_name": {
                                "english": "Molar Conductivity (Λm)",
                                "hindi": "मोलर चालकता (Λm)"
                            },
                            "description": {
                                "english": "Λm = κ / c\nUnits: S m² mol⁻¹ or S cm² mol⁻¹.\nIncreases with dilution.\nΛm⁰ = Limiting molar conductivity (at infinite dilution).",
                                "hindi": "Λm = κ / c\nमात्रक: S m² mol⁻¹ या S cm² mol⁻¹।\nतनुता के साथ बढ़ती है।\nΛm⁰ = सीमांत मोलर चालकता (अनंत तनुता पर)।"
                            }
                        }
                    ]
                },
                {
                    "id": "topic2_5",
                    "display_name": {
                        "english": "KOHLRAUSCH'S LAW",
                        "hindi": "कोलराऊश का नियम"
                    },
                    "article_range": "Section 2.4.2",
                    "concepts": [
                        {
                            "id": "concept2_5_1",
                            "display_name": {
                                "english": "Independent Migration of Ions",
                                "hindi": "आयनों का स्वतंत्र प्रवासन"
                            },
                            "description": {
                                "english": "Λm⁰ = ν⁺λ⁺⁰ + ν⁻λ⁻⁰\nλ⁺⁰ and λ⁻⁰ are limiting molar conductivities of cation and anion.\nUsed to find Λm⁰ of weak electrolytes and degree of dissociation (α = Λm/Λm⁰).",
                                "hindi": "Λm⁰ = ν⁺λ⁺⁰ + ν⁻λ⁻⁰\nλ⁺⁰ और λ⁻⁰ धनायन एवं ऋणायन की सीमांत मोलर चालकताएं हैं।\nदुर्बल विद्युत अपघट्यों का Λm⁰ और वियोजन की मात्रा (α = Λm/Λm⁰) ज्ञात करने में प्रयुक्त।"
                            }
                        }
                    ]
                },
                {
                    "id": "topic2_6",
                    "display_name": {
                        "english": "ELECTROLYSIS AND FARADAY'S LAWS",
                        "hindi": "विद्युत अपघटन एवं फैराडे के नियम"
                    },
                    "article_range": "Section 2.5",
                    "concepts": [
                        {
                            "id": "concept2_6_1",
                            "display_name": {
                                "english": "Faraday's Laws of Electrolysis",
                                "hindi": "विद्युत अपघटन के फैराडे नियम"
                            },
                            "description": {
                                "english": "• First Law: Amount of substance deposited/produced is proportional to quantity of electricity (Q = It).\n• Second Law: Amounts of different substances produced by same Q are proportional to their chemical equivalent weights.\n1 F = 96487 C mol⁻¹ ≈ 96500 C mol⁻¹.",
                                "hindi": "• प्रथम नियम: निक्षेपित/उत्पन्न पदार्थ की मात्रा, विद्युत की मात्रा (Q = It) के समानुपाती होती है।\n• द्वितीय नियम: समान Q द्वारा उत्पन्न विभिन्न पदार्थों की मात्राएं, उनके रासायनिक तुल्यांकी भारों के समानुपाती होती हैं।\n1 F = 96487 C mol⁻¹ ≈ 96500 C mol⁻¹."
                            }
                        }
                    ]
                },
                {
                    "id": "topic2_7",
                    "display_name": {
                        "english": "BATTERIES AND CORROSION",
                        "hindi": "बैटरियाँ एवं संक्षारण"
                    },
                    "article_range": "Sections 2.6-2.8",
                    "concepts": [
                        {
                            "id": "concept2_7_1",
                            "display_name": {
                                "english": "Primary Batteries",
                                "hindi": "प्राथमिक बैटरियाँ"
                            },
                            "description": {
                                "english": "Non-rechargeable. Example: Dry cell (Leclanche cell).\nAnode: Zn → Zn²⁺ + 2e⁻\nCathode: MnO₂ + NH₄⁺ + e⁻ → MnO(OH) + NH₃\nVoltage ~ 1.5 V.",
                                "hindi": "अ-पुनर्भरणीय। उदाहरण: शुष्क सेल (लेक्लांची सेल)।\nएनोड: Zn → Zn²⁺ + 2e⁻\nकैथोड: MnO₂ + NH₄⁺ + e⁻ → MnO(OH) + NH₃\nवोल्टता ~ 1.5 V."
                            }
                        },
                        {
                            "id": "concept2_7_2",
                            "display_name": {
                                "english": "Secondary Batteries",
                                "hindi": "द्वितीयक बैटरियाँ"
                            },
                            "description": {
                                "english": "Rechargeable. Example: Lead storage battery.\nAnode (discharge): Pb + SO₄²⁻ → PbSO₄ + 2e⁻\nCathode (discharge): PbO₂ + SO₄²⁻ + 4H⁺ + 2e⁻ → PbSO₄ + 2H₂O\nOverall: Pb + PbO₂ + 2H₂SO₄ ⇌ 2PbSO₄ + 2H₂O",
                                "hindi": "पुनर्भरणीय। उदाहरण: लेड संचायक बैटरी।\nएनोड (निर्वहन): Pb + SO₄²⁻ → PbSO₄ + 2e⁻\nकैथोड (निर्वहन): PbO₂ + SO₄²⁻ + 4H⁺ + 2e⁻ → PbSO₄ + 2H₂O\nकुल: Pb + PbO₂ + 2H₂SO₄ ⇌ 2PbSO₄ + 2H₂O"
                            }
                        },
                        {
                            "id": "concept2_7_3",
                            "display_name": {
                                "english": "Fuel Cells",
                                "hindi": "ईंधन सेल"
                            },
                            "description": {
                                "english": "Galvanic cells with continuous supply of reactants.\nExample: H₂-O₂ fuel cell.\nAnode: 2H₂ + 4OH⁻ → 4H₂O + 4e⁻\nCathode: O₂ + 2H₂O + 4e⁻ → 4OH⁻\nBy-product is water.",
                                "hindi": "अभिकारकों की सतत आपूर्ति वाली गैल्वेनी सेल।\nउदाहरण: H₂-O₂ ईंधन सेल।\nएनोड: 2H₂ + 4OH⁻ → 4H₂O + 4e⁻\nकैथोड: O₂ + 2H₂O + 4e⁻ → 4OH⁻\nउपोत्पाद जल है।"
                            }
                        },
                        {
                            "id": "concept2_7_4",
                            "display_name": {
                                "english": "Corrosion (Rusting of Iron)",
                                "hindi": "संक्षारण (लोहे में जंग लगना)"
                            },
                            "description": {
                                "english": "Electrochemical phenomenon.\nAnodic area: 2Fe → 2Fe²⁺ + 4e⁻\nCathodic area: O₂ + 4H⁺ + 4e⁻ → 2H₂O\nOverall: 2Fe + O₂ + 4H⁺ → 2Fe²⁺ + 2H₂O\nFe²⁺ further oxidized to rust (Fe₂O₃.xH₂O).",
                                "hindi": "वैद्युत रासायनिक परिघटना।\nएनोडिक क्षेत्र: 2Fe → 2Fe²⁺ + 4e⁻\nकैथोडिक क्षेत्र: O₂ + 4H⁺ + 4e⁻ → 2H₂O\nकुल: 2Fe + O₂ + 4H⁺ → 2Fe²⁺ + 2H₂O\nFe²⁺ आगे ऑक्सीकृत होकर जंग (Fe₂O₃.xH₂O) बनाता है।"
                            }
                        }
                    ]
                }
            ]
        },
        # ============================================
        # CHAPTER 3: CHEMICAL KINETICS
        # ============================================
        {
            "id": "chapter3",
            "display_name": {
                "english": "CHAPTER 3: CHEMICAL KINETICS",
                "hindi": "अध्याय 3: रासायनिक बलगतिकी"
            },
            "color": "#138808",
            "topics": [
                {
                    "id": "topic3_1",
                    "display_name": {
                        "english": "RATE OF A REACTION",
                        "hindi": "अभिक्रिया की दर"
                    },
                    "article_range": "Section 3.1",
                    "concepts": [
                        {
                            "id": "concept3_1_1",
                            "display_name": {
                                "english": "Average and Instantaneous Rate",
                                "hindi": "औसत एवं तात्क्षणिक दर"
                            },
                            "description": {
                                "english": "Average rate: r_av = -Δ[R]/Δt = +Δ[P]/Δt\nInstantaneous rate: r_inst = -d[R]/dt = +d[P]/dt\nUnits: mol L⁻¹ s⁻¹ or atm s⁻¹ for gases.",
                                "hindi": "औसत दर: r_av = -Δ[R]/Δt = +Δ[P]/Δt\nतात्क्षणिक दर: r_inst = -d[R]/dt = +d[P]/dt\nमात्रक: mol L⁻¹ s⁻¹ या गैसों के लिए atm s⁻¹."
                            }
                        },
                        {
                            "id": "concept3_1_2",
                            "display_name": {
                                "english": "Stoichiometry and Rate",
                                "hindi": "स्टॉइकियोमिति एवं दर"
                            },
                            "description": {
                                "english": "For reaction: aA + bB → cC + dD\nRate = -(1/a)d[A]/dt = -(1/b)d[B]/dt = +(1/c)d[C]/dt = +(1/d)d[D]/dt",
                                "hindi": "अभिक्रिया के लिए: aA + bB → cC + dD\nदर = -(1/a)d[A]/dt = -(1/b)d[B]/dt = +(1/c)d[C]/dt = +(1/d)d[D]/dt"
                            }
                        }
                    ]
                },
                {
                    "id": "topic3_2",
                    "display_name": {
                        "english": "RATE LAW AND ORDER",
                        "hindi": "दर नियम एवं कोटि"
                    },
                    "article_range": "Section 3.2",
                    "concepts": [
                        {
                            "id": "concept3_2_1",
                            "display_name": {
                                "english": "Rate Law",
                                "hindi": "दर नियम"
                            },
                            "description": {
                                "english": "Rate = k[A]ˣ[B]ʸ\nk = rate constant.\nExponents x and y are determined experimentally.\nOrder of reaction = x + y",
                                "hindi": "दर = k[A]ˣ[B]ʸ\nk = दर स्थिरांक।\nघातांक x और y प्रयोगात्मक रूप से निर्धारित होते हैं।\nअभिक्रिया की कोटि = x + y"
                            }
                        },
                        {
                            "id": "concept3_2_2",
                            "display_name": {
                                "english": "Units of Rate Constant",
                                "hindi": "दर स्थिरांक के मात्रक"
                            },
                            "description": {
                                "english": "For overall order n: Units of k = (mol L⁻¹)¹⁻ⁿ s⁻¹\nZero order: mol L⁻¹ s⁻¹\nFirst order: s⁻¹\nSecond order: mol⁻¹ L s⁻¹",
                                "hindi": "कुल कोटि n के लिए: k के मात्रक = (mol L⁻¹)¹⁻ⁿ s⁻¹\nशून्य कोटि: mol L⁻¹ s⁻¹\nप्रथम कोटि: s⁻¹\nद्वितीय कोटि: mol⁻¹ L s⁻¹"
                            }
                        }
                    ]
                },
                {
                    "id": "topic3_3",
                    "display_name": {
                        "english": "INTEGRATED RATE LAWS",
                        "hindi": "समाकलित दर नियम"
                    },
                    "article_range": "Section 3.3",
                    "concepts": [
                        {
                            "id": "concept3_3_1",
                            "display_name": {
                                "english": "Zero Order Reactions",
                                "hindi": "शून्य कोटि अभिक्रियाएं"
                            },
                            "description": {
                                "english": "Rate = k\n[R] = -kt + [R]₀\nHalf-life: t₁/₂ = [R]₀ / 2k",
                                "hindi": "दर = k\n[R] = -kt + [R]₀\nअर्धायु: t₁/₂ = [R]₀ / 2k"
                            }
                        },
                        {
                            "id": "concept3_3_2",
                            "display_name": {
                                "english": "First Order Reactions",
                                "hindi": "प्रथम कोटि अभिक्रियाएं"
                            },
                            "description": {
                                "english": "Rate = k[R]\n[R] = [R]₀ e⁻ᵏᵗ\nln[R] = -kt + ln[R]₀\nk = (2.303/t) log([R]₀/[R])\nHalf-life: t₁/₂ = 0.693/k (independent of [R]₀)",
                                "hindi": "दर = k[R]\n[R] = [R]₀ e⁻ᵏᵗ\nln[R] = -kt + ln[R]₀\nk = (2.303/t) log([R]₀/[R])\nअर्धायु: t₁/₂ = 0.693/k ([R]₀ से स्वतंत्र)"
                            }
                        }
                    ]
                },
                {
                    "id": "topic3_4",
                    "display_name": {
                        "english": "TEMPERATURE DEPENDENCE",
                        "hindi": "तापमान पर निर्भरता"
                    },
                    "article_range": "Section 3.4",
                    "concepts": [
                        {
                            "id": "concept3_4_1",
                            "display_name": {
                                "english": "Arrhenius Equation",
                                "hindi": "आर्रेनियस समीकरण"
                            },
                            "description": {
                                "english": "k = A e⁻ᴱᵃ/ᴿᵀ\nA = Arrhenius factor/frequency factor\nEa = activation energy (J mol⁻¹)\nln k = -Ea/RT + ln A\nlog(k₂/k₁) = (Ea/2.303R)[(T₂-T₁)/(T₁T₂)]",
                                "hindi": "k = A e⁻ᴱᵃ/ᴿᵀ\nA = आर्रेनियस गुणांक/आवृत्ति गुणांक\nEa = सक्रियण ऊर्जा (J mol⁻¹)\nln k = -Ea/RT + ln A\nlog(k₂/k₁) = (Ea/2.303R)[(T₂-T₁)/(T₁T₂)]"
                            }
                        },
                        {
                            "id": "concept3_4_2",
                            "display_name": {
                                "english": "Activation Energy",
                                "hindi": "सक्रियण ऊर्जा"
                            },
                            "description": {
                                "english": "Minimum energy required for reaction to occur.\nReaction coordinate diagram: Reactants → Activated complex → Products.\nCatalyst provides alternate pathway with lower Ea.",
                                "hindi": "अभिक्रिया होने के लिए आवश्यक न्यूनतम ऊर्जा।\nअभिक्रिया निर्देशांक आरेख: अभिकारक → सक्रिय संकुल → उत्पाद।\nउत्प्रेरक कम Ea वाला वैकल्पिक पथ प्रदान करता है।"
                            }
                        }
                    ]
                },
                {
                    "id": "topic3_5",
                    "display_name": {
                        "english": "COLLISION THEORY",
                        "hindi": "संघट्ट सिद्धांत"
                    },
                    "article_range": "Section 3.4",
                    "concepts": [
                        {
                            "id": "concept3_5_1",
                            "display_name": {
                                "english": "Effective Collisions",
                                "hindi": "प्रभावी संघट्ट"
                            },
                            "description": {
                                "english": "Rate = P Z_AB e⁻ᴱᵃ/ᴿᵀ\nZ_AB = collision frequency\nP = steric factor (orientation requirement)\nEffective collisions require threshold energy and proper orientation.",
                                "hindi": "दर = P Z_AB e⁻ᴱᵃ/ᴿᵀ\nZ_AB = संघट्ट आवृत्ति\nP = स्टीरिक गुणांक (अभिविन्यास आवश्यकता)\nप्रभावी संघट्ट के लिए देहली ऊर्जा और सही अभिविन्यास आवश्यक है।"
                            }
                        }
                    ]
                }
            ]
        },
        # ============================================
        # CHAPTER 4: THE d- AND f- BLOCK ELEMENTS
        # ============================================
        {
            "id": "chapter4",
            "display_name": {
                "english": "CHAPTER 4: THE d- AND f- BLOCK ELEMENTS",
                "hindi": "अध्याय 4: d- एवं f- ब्लॉक के तत्व"
            },
            "color": "#FFD700",
            "topics": [
                {
                    "id": "topic4_1",
                    "display_name": {
                        "english": "GENERAL PROPERTIES OF d-BLOCK",
                        "hindi": "d-ब्लॉक के सामान्य गुण"
                    },
                    "article_range": "Sections 4.1-4.3",
                    "concepts": [
                        {
                            "id": "concept4_1_1",
                            "display_name": {
                                "english": "Electronic Configuration",
                                "hindi": "इलेक्ट्रॉनिक विन्यास"
                            },
                            "description": {
                                "english": "General: (n-1)d¹⁻¹⁰ ns¹⁻².\nExceptions due to stability of half-filled and fully filled d orbitals (e.g., Cr: 3d⁵4s¹, Cu: 3d¹⁰4s¹).",
                                "hindi": "सामान्य: (n-1)d¹⁻¹⁰ ns¹⁻².\nअर्धपूरित एवं पूर्णतः पूरित d कक्षकों की स्थिरता के कारण अपवाद (जैसे, Cr: 3d⁵4s¹, Cu: 3d¹⁰4s¹)."
                            }
                        },
                        {
                            "id": "concept4_1_2",
                            "display_name": {
                                "english": "Oxidation States",
                                "hindi": "ऑक्सीकरण अवस्थाएं"
                            },
                            "description": {
                                "english": "Show variable oxidation states due to small energy difference between (n-1)d and ns orbitals.\nMaximum oxidation state increases to middle (Mn, +7) then decreases.\nStability of +2 state increases across 3d series.",
                                "hindi": "(n-1)d और ns कक्षकों के बीच कम ऊर्जा अंतर के कारण परिवर्तनशील ऑक्सीकरण अवस्थाएं दर्शाते हैं।\nअधिकतम ऑक्सीकरण अवस्था मध्य तक बढ़ती है (Mn, +7) फिर घटती है।\n3d श्रेणी में +2 अवस्था की स्थिरता बढ़ती है।"
                            }
                        },
                        {
                            "id": "concept4_1_3",
                            "display_name": {
                                "english": "Atomic and Ionic Sizes",
                                "hindi": "परमाणु एवं आयनिक आकार"
                            },
                            "description": {
                                "english": "Radii decrease across a series due to poor shielding of d electrons.\nLanthanoid contraction: Radii of 4d and 5d series elements are similar.",
                                "hindi": "d-इलेक्ट्रॉनों के अप्रभावी परिरक्षण के कारण एक श्रेणी में त्रिज्याएं घटती हैं।\nलैन्थेनॉइड संकुचन: 4d और 5d श्रेणी के तत्वों की त्रिज्याएं समान होती हैं।"
                            }
                        },
                        {
                            "id": "concept4_1_4",
                            "display_name": {
                                "english": "Ionisation Enthalpy",
                                "hindi": "आयनन एन्थैल्पी"
                            },
                            "description": {
                                "english": "Increases across series but irregularly.\nHigher values for configurations with greater stability (d⁵, d¹⁰).",
                                "hindi": "श्रेणी में बढ़ती है लेकिन अनियमित रूप से।\nअधिक स्थिर विन्यास (d⁵, d¹⁰) के लिए उच्च मान।"
                            }
                        },
                        {
                            "id": "concept4_1_5",
                            "display_name": {
                                "english": "Magnetic Properties",
                                "hindi": "चुंबकीय गुण"
                            },
                            "description": {
                                "english": "Paramagnetism due to unpaired electrons.\nSpin-only magnetic moment: μ = √(n(n+2)) BM.\nDiamagnetic if no unpaired electrons.",
                                "hindi": "अयुग्मित इलेक्ट्रॉनों के कारण अनुचुंबकत्व।\nकेवल प्रचक्रण चुंबकीय आघूर्ण: μ = √(n(n+2)) BM.\nयदि कोई अयुग्मित इलेक्ट्रॉन न हो तो प्रतिचुंबकीय।"
                            }
                        },
                        {
                            "id": "concept4_1_6",
                            "display_name": {
                                "english": "Colour and Catalytic Activity",
                                "hindi": "रंग एवं उत्प्रेरक सक्रियता"
                            },
                            "description": {
                                "english": "Colour due to d-d transitions (absorption in visible region).\nCatalytic activity due to variable oxidation states and ability to form complexes.",
                                "hindi": "d-d संक्रमणों के कारण रंग (दृश्य क्षेत्र में अवशोषण)।\nपरिवर्तनशील ऑक्सीकरण अवस्थाओं एवं संकुल बनाने की क्षमता के कारण उत्प्रेरक सक्रियता।"
                            }
                        }
                    ]
                },
                {
                    "id": "topic4_2",
                    "display_name": {
                        "english": "POTASSIUM DICHROMATE (K₂Cr₂O₇)",
                        "hindi": "पोटैशियम डाइक्रोमेट (K₂Cr₂O₇)"
                    },
                    "article_range": "Section 4.4.1",
                    "concepts": [
                        {
                            "id": "concept4_2_1",
                            "display_name": {
                                "english": "Preparation",
                                "hindi": "विधि"
                            },
                            "description": {
                                "english": "From chromite ore (FeCr₂O₄):\n1. Fusion with Na₂CO₃ in air: 4FeCr₂O₄ + 8Na₂CO₃ + 7O₂ → 8Na₂CrO₄ + 2Fe₂O₃ + 8CO₂\n2. Acidify Na₂CrO₄ solution: 2Na₂CrO₄ + 2H⁺ → Na₂Cr₂O₇ + 2Na⁺ + H₂O\n3. Treat with KCl: Na₂Cr₂O₇ + 2KCl → K₂Cr₂O₇ + 2NaCl",
                                "hindi": "क्रोमाइट अयस्क (FeCr₂O₄) से:\n1. वायु में Na₂CO₃ के साथ संगलन: 4FeCr₂O₄ + 8Na₂CO₃ + 7O₂ → 8Na₂CrO₄ + 2Fe₂O₃ + 8CO₂\n2. Na₂CrO₄ विलयन को अम्लीकृत करें: 2Na₂CrO₄ + 2H⁺ → Na₂Cr₂O₇ + 2Na⁺ + H₂O\n3. KCl के साथ उपचार: Na₂Cr₂O₇ + 2KCl → K₂Cr₂O₇ + 2NaCl"
                            }
                        },
                        {
                            "id": "concept4_2_2",
                            "display_name": {
                                "english": "Properties and Structure",
                                "hindi": "गुण एवं संरचना"
                            },
                            "description": {
                                "english": "Orange crystals. Chromate (CrO₄²⁻, yellow) and dichromate (Cr₂O₇²⁻, orange) interconvertible with pH.\n2CrO₄²⁻ + 2H⁺ ⇌ Cr₂O₇²⁻ + H₂O\nStrong oxidising agent in acidic medium: Cr₂O₇²⁻ + 14H⁺ + 6e⁻ → 2Cr³⁺ + 7H₂O (E⁰ = 1.33V).",
                                "hindi": "नारंगी क्रिस्टल। क्रोमेट (CrO₄²⁻, पीला) और डाइक्रोमेट (Cr₂O₇²⁻, नारंगी) pH के साथ परस्पर परिवर्तनीय।\n2CrO₄²⁻ + 2H⁺ ⇌ Cr₂O₇²⁻ + H₂O\nअम्लीय माध्यम में प्रबल ऑक्सीकारक: Cr₂O₇²⁻ + 14H⁺ + 6e⁻ → 2Cr³⁺ + 7H₂O (E⁰ = 1.33V)."
                            }
                        }
                    ]
                },
                {
                    "id": "topic4_3",
                    "display_name": {
                        "english": "POTASSIUM PERMANGANATE (KMnO₄)",
                        "hindi": "पोटैशियम परमैंगनेट (KMnO₄)"
                    },
                    "article_range": "Section 4.4.1",
                    "concepts": [
                        {
                            "id": "concept4_3_1",
                            "display_name": {
                                "english": "Preparation",
                                "hindi": "विधि"
                            },
                            "description": {
                                "english": "From pyrolusite (MnO₂):\n1. Fusion with KOH in air: 2MnO₂ + 4KOH + O₂ → 2K₂MnO₄ (green) + 2H₂O\n2. Disproportionation of manganate: 3MnO₄²⁻ + 4H⁺ → 2MnO₄⁻ + MnO₂ + 2H₂O\nOr electrolytic oxidation of K₂MnO₄.",
                                "hindi": "पायरोलुसाइट (MnO₂) से:\n1. वायु में KOH के साथ संगलन: 2MnO₂ + 4KOH + O₂ → 2K₂MnO₄ (हरा) + 2H₂O\n2. मैंगनेट का असमानुपातन: 3MnO₄²⁻ + 4H⁺ → 2MnO₄⁻ + MnO₂ + 2H₂O\nया K₂MnO₄ का विद्युत अपघटनी ऑक्सीकरण।"
                            }
                        },
                        {
                            "id": "concept4_3_2",
                            "display_name": {
                                "english": "Oxidising Properties",
                                "hindi": "ऑक्सीकारक गुण"
                            },
                            "description": {
                                "english": "Purple colour. Oxidising action depends on pH.\nIn acidic medium: MnO₄⁻ + 8H⁺ + 5e⁻ → Mn²⁺ + 4H₂O\nIn neutral/faintly alkaline: MnO₄⁻ + 2H₂O + 3e⁻ → MnO₂ + 4OH⁻\nIn strong alkaline: MnO₄⁻ + e⁻ → MnO₄²⁻",
                                "hindi": "बैंगनी रंग। ऑक्सीकारक क्रिया pH पर निर्भर करती है।\nअम्लीय माध्यम में: MnO₄⁻ + 8H⁺ + 5e⁻ → Mn²⁺ + 4H₂O\nउदासीन/अल्प क्षारीय में: MnO₄⁻ + 2H₂O + 3e⁻ → MnO₂ + 4OH⁻\nप्रबल क्षारीय में: MnO₄⁻ + e⁻ → MnO₄²⁻"
                            }
                        }
                    ]
                },
                {
                    "id": "topic4_4",
                    "display_name": {
                        "english": "LANTHANOIDS AND ACTINOIDS",
                        "hindi": "लैन्थेनॉइड एवं एक्टिनॉइड"
                    },
                    "article_range": "Sections 4.5-4.6",
                    "concepts": [
                        {
                            "id": "concept4_4_1",
                            "display_name": {
                                "english": "Lanthanoid Contraction",
                                "hindi": "लैन्थेनॉइड संकुचन"
                            },
                            "description": {
                                "english": "Regular decrease in atomic/ionic radii across the lanthanoid series due to poor shielding of 4f electrons.\nConsequences: Similar radii of 4d and 5d transition elements (e.g., Zr and Hf), making them difficult to separate.",
                                "hindi": "4f इलेक्ट्रॉनों के अप्रभावी परिरक्षण के कारण लैन्थेनॉइड श्रेणी में परमाणु/आयनिक त्रिज्याओं में नियमित कमी।\nपरिणाम: 4d और 5d संक्रमण तत्वों की त्रिज्याएं समान (जैसे, Zr और Hf), जिससे उनका पृथक्करण कठिन होता है।"
                            }
                        },
                        {
                            "id": "concept4_4_2",
                            "display_name": {
                                "english": "Lanthanoids vs Actinoids",
                                "hindi": "लैन्थेनॉइड बनाम एक्टिनॉइड"
                            },
                            "description": {
                                "english": "• Lanthanoids: Principal oxidation state +3; 4f orbitals deeply buried.\n• Actinoids: Greater range of oxidation states (+3 to +7); 5f orbitals less buried, participate in bonding; radioactive; actinoid contraction greater than lanthanoid contraction.",
                                "hindi": "• लैन्थेनॉइड: मुख्य ऑक्सीकरण अवस्था +3; 4f कक्षक गहरे दबे होते हैं।\n• एक्टिनॉइड: ऑक्सीकरण अवस्थाओं की अधिक विस्तृत श्रृंखला (+3 से +7); 5f कक्षक कम दबे होते हैं, आबंधन में भाग लेते हैं; रेडियोधर्मी; एक्टिनॉइड संकुचन लैन्थेनॉइड संकुचन से अधिक होता है।"
                            }
                        }
                    ]
                }
            ]
        },
           
        # ============================================
        # CHAPTER 5: COORDINATION COMPOUNDS
        # ============================================
        {
            "id": "chapter5",
            "display_name": {
                "english": "CHAPTER 5: COORDINATION COMPOUNDS",
                "hindi": "अध्याय 5: उपसहसंयोजन यौगिक"
            },
            "color": "#FF9933",
            "topics": [
                {
                    "id": "topic5_1",
                    "display_name": {
                        "english": "WERNER'S THEORY",
                        "hindi": "वर्नर का सिद्धांत"
                    },
                    "article_range": "Section 5.1",
                    "concepts": [
                        {
                            "id": "concept5_1_1",
                            "display_name": {
                                "english": "Primary and Secondary Valences",
                                "hindi": "प्राथमिक एवं द्वितीयक संयोजकताएं"
                            },
                            "description": {
                                "english": "• Primary valence: Ionisable, corresponds to oxidation state, satisfied by negative ions.\n• Secondary valence: Non-ionisable, corresponds to coordination number, satisfied by ligands.\n• Coordination sphere: Central metal + ligands (enclosed in []). Counter ions are outside.",
                                "hindi": "• प्राथमिक संयोजकता: आयनीय, ऑक्सीकरण अवस्था के अनुरूप, ऋणायनों द्वारा संतुष्ट।\n• द्वितीयक संयोजकता: अनायनीय, उपसहसंयोजन संख्या के अनुरूप, लिगेंड द्वारा संतुष्ट।\n• उपसहसंयोजन क्षेत्र: केंद्रीय धातु + लिगेंड ([] में). प्रतिआयन बाहर होते हैं।"
                            }
                        }
                    ]
                },
                {
                    "id": "topic5_2",
                    "display_name": {
                        "english": "DEFINITIONS AND NOMENCLATURE",
                        "hindi": "परिभाषाएं एवं नामकरण"
                    },
                    "article_range": "Sections 5.2-5.3",
                    "concepts": [
                        {
                            "id": "concept5_2_1",
                            "display_name": {
                                "english": "Important Terms",
                                "hindi": "महत्वपूर्ण पद"
                            },
                            "description": {
                                "english": "• Ligand: Ion/molecule bound to central atom. Unidentate (one donor atom), didentate, polydentate, ambidentate (e.g., NO₂⁻, SCN⁻).\n• Chelate: Complex with di/polydentate ligand forming a ring.\n• Coordination number: Number of ligand donor atoms bonded to central metal.",
                                "hindi": "• लिगेंड: केंद्रीय परमाणु से बंधित आयन/अणु। एकदंतुर, द्विदंतुर, बहुदंतुर, उभयदंतुर (जैसे, NO₂⁻, SCN⁻).\n• चीलेट: द्वि/बहुदंतुर लिगेंड वाला संकुल जो वलय बनाता है।\n• उपसहसंयोजन संख्या: केंद्रीय धातु से बंधित लिगेंड दाता परमाणुओं की संख्या।"
                            }
                        },
                        {
                            "id": "concept5_2_2",
                            "display_name": {
                                "english": "IUPAC Naming Rules",
                                "hindi": "IUPAC नामकरण नियम"
                            },
                            "description": {
                                "english": "• Cation named first, then anion.\n• Ligands in alphabetical order (ignoring prefixes).\n• Anionic ligands end in -o (chlorido, cyanido). Neutral: aqua (H₂O), ammine (NH₃), carbonyl (CO).\n• Prefixes: di, tri, tetrakis etc.\n• Oxidation state of metal in Roman numerals.\n• Metal name ends with -ate if complex is anion.",
                                "hindi": "• धनायन पहले, फिर ऋणायन।\n• लिगेंड वर्णानुक्रम में (उपसर्गों को छोड़कर)।\n• ऋणायनी लिगेंड -o में समाप्त होते हैं (क्लोरिडो, सायनिडो)। उदासीन: एक्वा (H₂O), अम्मीन (NH₃), कार्बोनिल (CO).\n• उपसर्ग: डाइ, ट्राइ, टेट्राकिस आदि।\n• धातु की ऑक्सीकरण अवस्था रोमन अंकों में।\n• यदि संकुल ऋणायन है तो धातु का नाम -एट में समाप्त होता है।"
                            }
                        }
                    ]
                },
                {
                    "id": "topic5_3",
                    "display_name": {
                        "english": "ISOMERISM",
                        "hindi": "समावयवता"
                    },
                    "article_range": "Section 5.4",
                    "concepts": [
                        {
                            "id": "concept5_3_1",
                            "display_name": {
                                "english": "Geometrical Isomerism",
                                "hindi": "ज्यामितीय समावयवता"
                            },
                            "description": {
                                "english": "Different spatial arrangements of ligands.\nIn square planar [Ma₂b₂]: cis and trans.\nIn octahedral [Ma₄b₂]: cis and trans. [Ma₃b₃]: fac and mer.",
                                "hindi": "लिगेंडों की विभिन्न स्थानिक व्यवस्थाएं।\nवर्ग समतलीय [Ma₂b₂] में: सिस और ट्रांस।\nअष्टफलकीय [Ma₄b₂] में: सिस और ट्रांस। [Ma₃b₃] में: फैक और मेर।"
                            }
                        },
                        {
                            "id": "concept5_3_2",
                            "display_name": {
                                "english": "Optical Isomerism",
                                "hindi": "प्रकाशिक समावयवता"
                            },
                            "description": {
                                "english": "Chiral complexes rotate plane-polarised light.\nEnantiomers are non-superimposable mirror images.\nCommon in octahedral complexes with chelating ligands (e.g., [Co(en)₃]³⁺).",
                                "hindi": "काइरल संकुल समतल-ध्रुवित प्रकाश को घुमाते हैं।\nप्रतिबिंब समावयवी (एनैन्टियोमर) अध्यारोपित न होने वाली दर्पण प्रतिबिंब होते हैं।\nचीलेटिंग लिगेंड वाले अष्टफलकीय संकुलों में सामान्य (जैसे, [Co(en)₃]³⁺)."
                            }
                        },
                        {
                            "id": "concept5_3_3",
                            "display_name": {
                                "english": "Structural Isomerism",
                                "hindi": "संरचनात्मक समावयवता"
                            },
                            "description": {
                                "english": "• Linkage: Ambidentate ligand binds through different atoms (e.g., [Co(NH₃)₅(NO₂)]Cl₂ vs [Co(NH₃)₅(ONO)]Cl₂).\n• Ionisation: Counter ion is also a ligand (e.g., [Co(NH₃)₅SO₄]Br vs [Co(NH₃)₅Br]SO₄).\n• Coordination: Interchange of ligands between cation and anion.\n• Solvate: Water molecule is either coordinated or as solvent of crystallisation.",
                                "hindi": "• उपसहसंयोजन: उभयदंतुर लिगेंड भिन्न परमाणुओं से बंधता है (जैसे, [Co(NH₃)₅(NO₂)]Cl₂ बनाम [Co(NH₃)₅(ONO)]Cl₂).\n• आयनन: प्रतिआयन भी एक लिगेंड होता है (जैसे, [Co(NH₃)₅SO₄]Br बनाम [Co(NH₃)₅Br]SO₄).\n• उपसहसंयोजन: धनायन और ऋणायन के बीच लिगेंडों का अदला-बदली।\n• विलायक: जल अणु या तो उपसहसंयोजित होता है या क्रिस्टलीकरण के विलायक के रूप में।"
                            }
                        }
                    ]
                },
                {
                    "id": "topic5_4",
                    "display_name": {
                        "english": "BONDING THEORIES",
                        "hindi": "आबंधन सिद्धांत"
                    },
                    "article_range": "Sections 5.5",
                    "concepts": [
                        {
                            "id": "concept5_4_1",
                            "display_name": {
                                "english": "Valence Bond Theory (VBT)",
                                "hindi": "संयोजकता आबंध सिद्धांत (VBT)"
                            },
                            "description": {
                                "english": "Metal uses (n-1)d, ns, np orbitals to hybridise.\nLigands donate electron pairs to hybrid orbitals.\nExplains geometry and magnetism.\n• Inner orbital/low spin complexes: use (n-1)d orbitals for d²sp³ hybridisation (e.g., [Co(NH₃)₆]³⁺).\n• Outer orbital/high spin complexes: use nd orbitals for sp³d² hybridisation (e.g., [CoF₆]³⁻).",
                                "hindi": "धातु (n-1)d, ns, np कक्षकों का संकरण करती है।\nलिगेंड संकर कक्षकों को इलेक्ट्रॉन युग्म प्रदान करते हैं।\nज्यामिति और चुंबकत्व की व्याख्या करता है।\n• आंतर कक्षीय/निम्न प्रचक्रण संकुल: d²sp³ संकरण के लिए (n-1)d कक्षकों का उपयोग (जैसे, [Co(NH₃)₆]³⁺).\n• बाह्य कक्षीय/उच्च प्रचक्रण संकुल: sp³d² संकरण के लिए nd कक्षकों का उपयोग (जैसे, [CoF₆]³⁻)."
                            }
                        },
                        {
                            "id": "concept5_4_2",
                            "display_name": {
                                "english": "Crystal Field Theory (CFT)",
                                "hindi": "क्रिस्टल क्षेत्र सिद्धांत (CFT)"
                            },
                            "description": {
                                "english": "Electrostatic model: Metal-ligand bond is ionic.\nIn octahedral field, d orbitals split into t₂g (lower energy: dxy, dyz, dxz) and eg (higher energy: dx²-y², dz²).\nCrystal Field Splitting Energy (Δ₀).\nStrong field ligands (CN⁻, CO) cause large Δ₀ → low spin complexes. Weak field ligands (H₂O, Cl⁻) cause small Δ₀ → high spin complexes.",
                                "hindi": "स्थिरवैद्युत मॉडल: धातु-लिगेंड आबंध आयनिक है।\nअष्टफलकीय क्षेत्र में, d कक्षक t₂g (निम्न ऊर्जा: dxy, dyz, dxz) और eg (उच्च ऊर्जा: dx²-y², dz²) में विभाजित हो जाते हैं।\nक्रिस्टल क्षेत्र विपाटन ऊर्जा (Δ₀).\nप्रबल क्षेत्र लिगेंड (CN⁻, CO) बड़ा Δ₀ उत्पन्न करते हैं → निम्न प्रचक्रण संकुल। दुर्बल क्षेत्र लिगेंड (H₂O, Cl⁻) छोटा Δ₀ उत्पन्न करते हैं → उच्च प्रचक्रण संकुल।"
                            }
                        },
                        {
                            "id": "concept5_4_3",
                            "display_name": {
                                "english": "Colour and CFT",
                                "hindi": "रंग एवं CFT"
                            },
                            "description": {
                                "english": "Colour arises from d-d transitions of electrons from lower to higher d orbitals.\nEnergy difference (Δ) corresponds to wavelength of light absorbed.\nComplex shows colour complementary to absorbed light.",
                                "hindi": "रंग, इलेक्ट्रॉनों के निचले d कक्षक से उच्च d कक्षक में d-d संक्रमण के कारण होता है।\nऊर्जा अंतर (Δ), अवशोषित प्रकाश की तरंगदैर्घ्य के अनुरूप होता है।\nसंकुल, अवशोषित प्रकाश के पूरक रंग का दिखता है।"
                            }
                        }
                    ]
                },
                {
                    "id": "topic5_5",
                    "display_name": {
                        "english": "METAL CARBONYLS AND APPLICATIONS",
                        "hindi": "धातु कार्बोनिल एवं अनुप्रयोग"
                    },
                    "article_range": "Sections 5.6-5.7",
                    "concepts": [
                        {
                            "id": "concept5_5_1",
                            "display_name": {
                                "english": "Metal Carbonyl Bonding",
                                "hindi": "धातु कार्बोनिल आबंधन"
                            },
                            "description": {
                                "english": "Synergic bonding: CO donates lone pair to metal (σ bond) and metal donates electron density back to π* orbital of CO (π back bonding). This strengthens the M-C bond.",
                                "hindi": "सहक्रियात्मक आबंधन: CO धातु को एकाकी इलेक्ट्रॉन युग्म दान करता है (σ आबंध) और धातु CO के π* कक्षक में वापस इलेक्ट्रॉन घनत्व दान करती है (π पश्च आबंधन)। यह M-C आबंध को मजबूत करता है।"
                            }
                        },
                        {
                            "id": "concept5_5_2",
                            "display_name": {
                                "english": "Applications",
                                "hindi": "अनुप्रयोग"
                            },
                            "description": {
                                "english": "• Qualitative/quantitative analysis (e.g., Ni with DMG).\n• Extraction of metals (e.g., Au, Ag with CN⁻).\n• Purification of metals (e.g., Ni via [Ni(CO)₄]).\n• Biological systems: Chlorophyll (Mg), Haemoglobin (Fe), Vitamin B₁₂ (Co).\n• Catalysts (e.g., Wilkinson's catalyst).\n• Medicine (e.g., cis-platin in cancer treatment).",
                                "hindi": "• गुणात्मक/मात्रात्मक विश्लेषण (जैसे, DMG के साथ Ni).\n• धातुओं का निष्कर्षण (जैसे, CN⁻ के साथ Au, Ag).\n• धातुओं का शोधन (जैसे, [Ni(CO)₄] के माध्यम से Ni).\n• जैविक तंत्र: क्लोरोफिल (Mg), हीमोग्लोबिन (Fe), विटामिन B₁₂ (Co).\n• उत्प्रेरक (जैसे, विल्किंसन उत्प्रेरक).\n• चिकित्सा (जैसे, कैंसर उपचार में सिस-प्लैटिन)."
                            }
                        }
                    ]
                }
            ]

        },

    # ============================================
# CHAPTER 6: HALOALKANES AND HALOARENES
# ============================================
{
    "id": "chapter6",
    "display_name": {
        "english": "CHAPTER 6: HALOALKANES AND HALOARENES",
        "hindi": "अध्याय 6: हैलोऐल्केन तथा हैलोऐरीन"
    },
    "color": "#0066CC",
    "topics": [
        {
            "id": "topic6_1",
            "display_name": {
                "english": "CLASSIFICATION AND NOMENCLATURE",
                "hindi": "वर्गीकरण एवं नामकरण"
            },
            "article_range": "Sections 6.1-6.2",
            "concepts": [
                {
                    "id": "concept6_1_1",
                    "display_name": {
                        "english": "Classification",
                        "hindi": "वर्गीकरण"
                    },
                    "description": {
                        "english": "• On the basis of number of halogen atoms: Mono, di, tri, polyhalogen compounds.\n• On the basis of sp³ C-X bond: Alkyl halides (primary, secondary, tertiary), allylic, benzylic.\n• On the basis of sp² C-X bond: Vinylic halides, aryl halides.",
                        "hindi": "• हैलोजन परमाणुओं की संख्या के आधार पर: मोनो, डाइ, ट्राइ, पॉलीहैलो यौगिक।\n• sp³ C-X बंध के आधार पर: एल्किल हैलाइड (प्राथमिक, द्वितीयक, तृतीयक), एलिलिक, बेंजिलिक।\n• sp² C-X बंध के आधार पर: वाइनिलिक हैलाइड, एरिल हैलाइड।"
                    }
                },
                {
                    "id": "concept6_1_2",
                    "display_name": {
                        "english": "Nomenclature",
                        "hindi": "नामकरण"
                    },
                    "description": {
                        "english": "• Common name: Alkyl group + halide (e.g., Ethyl chloride).\n• IUPAC name: Halo-substituted hydrocarbon (e.g., Chloroethane).\n• Gem-dihalides: Both halogens on same carbon (Alkylidene halides).\n• Vic-dihalides: Halogens on adjacent carbons (Alkylene dihalides).",
                        "hindi": "• साधारण नाम: एल्किल समूह + हैलाइड (जैसे, एथिल क्लोराइड)।\n• IUPAC नाम: हैलो-प्रतिस्थापित हाइड्रोकार्बन (जैसे, क्लोरोएथेन)।\n• जेम-डाइहैलाइड: दोनों हैलोजन एक ही कार्बन पर (एल्किलिडीन हैलाइड)।\n• विक-डाइहैलाइड: हैलोजन आसन्न कार्बनों पर (एल्किलीन डाइहैलाइड)।"
                    }
                },
                {
                    "id": "concept6_1_3",
                    "display_name": {
                        "english": "Nature of C-X Bond",
                        "hindi": "C-X बंध की प्रकृति"
                    },
                    "description": {
                        "english": "• Polar bond due to electronegativity difference (δ+ on C, δ- on X).\n• Bond length increases: C-F < C-Cl < C-Br < C-I.\n• Bond enthalpy decreases: C-F > C-Cl > C-Br > C-I.\n• Dipole moment decreases: CH₃Cl (1.86 D) > CH₃F (1.85 D) > CH₃Br (1.83 D) > CH₃I (1.64 D).",
                        "hindi": "• वैद्युतऋणात्मकता अंतर के कारण ध्रुवीय बंध (C पर δ+, X पर δ-).\n• बंध लंबाई बढ़ती है: C-F < C-Cl < C-Br < C-I.\n• बंध एन्थैल्पी घटती है: C-F > C-Cl > C-Br > C-I.\n• द्विध्रुव आघूर्ण घटता है: CH₃Cl (1.86 D) > CH₃F (1.85 D) > CH₃Br (1.83 D) > CH₃I (1.64 D)."
                    }
                }
            ]
        },
        {
            "id": "topic6_2",
            "display_name": {
                "english": "METHODS OF PREPARATION",
                "hindi": "विधियाँ"
            },
            "article_range": "Sections 6.4-6.5",
            "concepts": [
                {
                    "id": "concept6_2_1",
                    "display_name": {
                        "english": "From Alcohols",
                        "hindi": "एल्कोहॉल से"
                    },
                    "description": {
                        "english": "• R-OH + HCl → R-Cl + H₂O (ZnCl₂ catalyst for 1°,2°; 3° reacts readily).\n• R-OH + PCl₅ → R-Cl + POCl₃ + HCl\n• R-OH + SOCl₂ (Thionyl chloride) → R-Cl + SO₂↑ + HCl↑ (Best method, gaseous byproducts escape).\n• R-OH + PBr₃ → R-Br + H₃PO₃\n• Reactivity order: 3° > 2° > 1°",
                        "hindi": "• R-OH + HCl → R-Cl + H₂O (1°,2° के लिए ZnCl₂ उत्प्रेरक; 3° सरलता से क्रिया करता है)।\n• R-OH + PCl₅ → R-Cl + POCl₃ + HCl\n• R-OH + SOCl₂ (थायोनिल क्लोराइड) → R-Cl + SO₂↑ + HCl↑ (सर्वोत्तम विधि, गैसीय उपोत्पाद बाहर निकल जाते हैं)।\n• R-OH + PBr₃ → R-Br + H₃PO₃\n• अभिक्रियाशीलता क्रम: 3° > 2° > 1°"
                    }
                },
                {
                    "id": "concept6_2_2",
                    "display_name": {
                        "english": "From Hydrocarbons",
                        "hindi": "हाइड्रोकार्बन से"
                    },
                    "description": {
                        "english": "• Free radical halogenation of alkanes (gives mixture, poor yield).\n• Addition of HX to alkenes (follows Markovnikov's rule).\n• Anti-Markovnikov addition with HBr in presence of peroxide.\n• Addition of halogens to alkenes gives vic-dihalides.",
                        "hindi": "• एल्केनों का मुक्त मूलक हैलोजनीकरण (मिश्रण मिलता है, कम उपज)।\n• एल्कीनों में HX का योग (मार्कोवनिकोव के नियम का पालन)।\n• पेरॉक्साइड की उपस्थिति में HBr का एंटी-मार्कोवनिकोव योग।\n• एल्कीनों में हैलोजन का योग विक-डाइहैलाइड देता है।"
                    }
                },
                {
                    "id": "concept6_2_3",
                    "display_name": {
                        "english": "Halogen Exchange",
                        "hindi": "हैलोजन विनिमय"
                    },
                    "description": {
                        "english": "• Finkelstein reaction: R-X + NaI (acetone) → R-I + NaX↓ (X = Cl, Br).\n• Swarts reaction: R-X + AgF/Hg₂F₂/CoF₂/SbF₃ → R-F (for preparing alkyl fluorides).",
                        "hindi": "• फिंकेल्स्टीन अभिक्रिया: R-X + NaI (एसीटोन) → R-I + NaX↓ (X = Cl, Br).\n• स्वार्ट्स अभिक्रिया: R-X + AgF/Hg₂F₂/CoF₂/SbF₃ → R-F (एल्किल फ्लोराइड बनाने के लिए)।"
                    }
                },
                {
                    "id": "concept6_2_4",
                    "display_name": {
                        "english": "Preparation of Haloarenes",
                        "hindi": "हैलोऐरीनों की विधि"
                    },
                    "description": {
                        "english": "• Electrophilic substitution of arenes: C₆H₆ + X₂ (Fe or FeX₃) → C₆H₅X + HX.\n• Sandmeyer's reaction: C₆H₅N₂⁺Cl⁻ + CuX/HX → C₆H₅X + N₂ (X = Cl, Br).\n• From diazonium salt with KI (no Cu required): C₆H₅N₂⁺Cl⁻ + KI → C₆H₅I + KCl + N₂.",
                        "hindi": "• ऐरीनों का इलेक्ट्रॉनस्नेही प्रतिस्थापन: C₆H₆ + X₂ (Fe या FeX₃) → C₆H₅X + HX.\n• सैंडमायर अभिक्रिया: C₆H₅N₂⁺Cl⁻ + CuX/HX → C₆H₅X + N₂ (X = Cl, Br).\n• डाइऐज़ोनियम लवण से KI के साथ (Cu की आवश्यकता नहीं): C₆H₅N₂⁺Cl⁻ + KI → C₆H₅I + KCl + N₂."
                    }
                }
            ]
        },
        {
            "id": "topic6_3",
            "display_name": {
                "english": "PHYSICAL PROPERTIES",
                "hindi": "भौतिक गुण"
            },
            "article_range": "Section 6.6",
            "concepts": [
                {
                    "id": "concept6_3_1",
                    "display_name": {
                        "english": "Boiling Points",
                        "hindi": "क्वथनांक"
                    },
                    "description": {
                        "english": "• Higher than hydrocarbons of comparable mass due to stronger dipole-dipole and van der Waals forces.\n• For same alkyl group: RI > RBr > RCl > RF (increasing size and mass).\n• Boiling point decreases with branching (isomeric haloalkanes).",
                        "hindi": "• तुलनीय द्रव्यमान के हाइड्रोकार्बनों से अधिक, प्रबल द्विध्रुव-द्विध्रुव एवं वान्डर वाल्स बलों के कारण।\n• समान एल्किल समूह के लिए: RI > RBr > RCl > RF (बढ़ते आकार एवं द्रव्यमान के साथ)।\n• शाखन के साथ क्वथनांक घटता है (समावयवी हैलोऐल्केनों में)।"
                    }
                },
                {
                    "id": "concept6_3_2",
                    "display_name": {
                        "english": "Density and Solubility",
                        "hindi": "घनत्व एवं विलेयता"
                    },
                    "description": {
                        "english": "• Bromo, iodo, polychloro derivatives are denser than water.\n• Density increases with number of halogen atoms and atomic mass.\n• Insoluble in water (cannot break H-bonds of water).\n• Soluble in organic solvents.",
                        "hindi": "• ब्रोमो, आयोडो, पॉलीक्लोरो व्युत्पन्न जल से सघन होते हैं।\n• घनत्व हैलोजन परमाणुओं की संख्या एवं परमाणु द्रव्यमान के साथ बढ़ता है।\n• जल में अविलेय (जल के H-बंध नहीं तोड़ सकते)।\n• कार्बनिक विलायकों में विलेय।"
                    }
                }
            ]
        },
        {
            "id": "topic6_4",
            "display_name": {
                "english": "CHEMICAL REACTIONS",
                "hindi": "रासायनिक अभिक्रियाएं"
            },
            "article_range": "Section 6.7",
            "concepts": [
                {
                    "id": "concept6_4_1",
                    "display_name": {
                        "english": "Nucleophilic Substitution (SN1 & SN2)",
                        "hindi": "नाभिकस्नेही प्रतिस्थापन (SN1 एवं SN2)"
                    },
                    "description": {
                        "english": "• SN2: Bimolecular, one step, inversion of configuration. Rate = k[RX][Nu]. Favoured by primary halides, strong nucleophiles, polar aprotic solvents.\n• SN1: Unimolecular, two steps via carbocation, racemisation. Rate = k[RX]. Favoured by tertiary halides, weak nucleophiles, polar protic solvents.\n• Reactivity order for SN2: CH₃X > 1° > 2° > 3°\n• Reactivity order for SN1: 3° > 2° > 1° > CH₃X",
                        "hindi": "• SN2: द्विअणुक, एक पद, विन्यास का उत्क्रमण। दर = k[RX][Nu]. प्राथमिक हैलाइड, प्रबल नाभिकस्नेही, ध्रुवीय अप्रोटिक विलायकों के लिए अनुकूल।\n• SN1: एकअणुक, दो पद (कार्बोकैटायन माध्यम से), रेसिमीकरण। दर = k[RX]. तृतीयक हैलाइड, दुर्बल नाभिकस्नेही, ध्रुवीय प्रोटिक विलायकों के लिए अनुकूल।\n• SN2 के लिए अभिक्रियाशीलता क्रम: CH₃X > 1° > 2° > 3°\n• SN1 के लिए अभिक्रियाशीलता क्रम: 3° > 2° > 1° > CH₃X"
                    }
                },
                {
                    "id": "concept6_4_2",
                    "display_name": {
                        "english": "Elimination Reactions",
                        "hindi": "विलोपन अभिक्रियाएं"
                    },
                    "description": {
                        "english": "• Dehydrohalogenation (β-elimination): R-X + alc. KOH → Alkene + KX + H₂O\n• Saytzeff's rule: More substituted alkene is the major product.\nExample: 2-Bromopentane gives pent-2-ene (major) and pent-1-ene (minor).",
                        "hindi": "• डिहाइड्रोहैलोजनीकरण (β-विलोपन): R-X + एल्को. KOH → एल्कीन + KX + H₂O\n• सायट्जेफ नियम: अधिक प्रतिस्थापित एल्कीन मुख्य उत्पाद होता है।\nउदाहरण: 2-ब्रोमोपेन्टेन पेन्ट-2-ईन (मुख्य) और पेन्ट-1-ईन (अल्प) देता है।"
                    }
                },
                {
                    "id": "concept6_4_3",
                    "display_name": {
                        "english": "Reactions with Metals",
                        "hindi": "धातुओं के साथ अभिक्रियाएं"
                    },
                    "description": {
                        "english": "• Grignard reagent: R-X + Mg (dry ether) → RMgX (alkyl magnesium halide). Highly reactive, must be prepared under anhydrous conditions.\n• Wurtz reaction: 2R-X + 2Na (dry ether) → R-R + 2NaX",
                        "hindi": "• ग्रिगनार्ड अभिकर्मक: R-X + Mg (शुष्क ईथर) → RMgX (एल्किल मैग्नीशियम हैलाइड)। अत्यधिक अभिक्रियाशील, निर्जल परिस्थितियों में बनाना चाहिए।\n• वुर्ट्ज अभिक्रिया: 2R-X + 2Na (शुष्क ईथर) → R-R + 2NaX"
                    }
                },
                {
                    "id": "concept6_4_4",
                    "display_name": {
                        "english": "Ambident Nucleophiles",
                        "hindi": "उभयदंती नाभिकस्नेही"
                    },
                    "description": {
                        "english": "• KCN (ionic) gives alkyl cyanides (R-CN) via C-attack.\n• AgCN (covalent) gives alkyl isocyanides (R-NC) via N-attack.\n• KNO₂ gives alkyl nitrites (R-O-N=O).\n• AgNO₂ gives nitroalkanes (R-NO₂).",
                        "hindi": "• KCN (आयनिक) C-आक्रमण द्वारा एल्किल सायनाइड (R-CN) देता है।\n• AgCN (सहसंयोजक) N-आक्रमण द्वारा एल्किल आइसोसायनाइड (R-NC) देता है।\n• KNO₂ एल्किल नाइट्राइट (R-O-N=O) देता है।\n• AgNO₂ नाइट्रोएल्केन (R-NO₂) देता है।"
                    }
                }
            ]
        },
        {
            "id": "topic6_5",
            "display_name": {
                "english": "POLYHALOGEN COMPOUNDS",
                "hindi": "बहुहैलोजन यौगिक"
            },
            "article_range": "Section 6.8",
            "concepts": [
                {
                    "id": "concept6_5_1",
                    "display_name": {
                        "english": "Important Polyhalogen Compounds",
                        "hindi": "महत्वपूर्ण बहुहैलोजन यौगिक"
                    },
                    "description": {
                        "english": "• Dichloromethane (CH₂Cl₂): Solvent, paint remover.\n• Chloroform (CHCl₃): Solvent, stored in dark bottles to prevent oxidation to phosgene (COCl₂).\n• Iodoform (CHI₃): Antiseptic.\n• Carbon tetrachloride (CCl₄): Fire extinguisher, refrigerant (now restricted due to ozone depletion).\n• Freons (CFCs): Refrigerants, propellants (cause ozone layer depletion).\n• DDT (C₁₄H₉Cl₅): Insecticide (now banned due to toxicity and persistence).",
                        "hindi": "• डाइक्लोरोमेथेन (CH₂Cl₂): विलायक, पेंट हटाने वाला।\n• क्लोरोफॉर्म (CHCl₃): विलायक, फॉस्जीन (COCl₂) बनने से रोकने के लिए गहरे रंग की बोतलों में रखते हैं।\n• आयोडोफॉर्म (CHI₃): एंटीसेप्टिक।\n• कार्बन टेट्राक्लोराइड (CCl₄): अग्निशामक, प्रशीतक (अब ओज़ोन ह्रास के कारण प्रतिबंधित)।\n• फ्रेऑन (CFCs): प्रशीतक, प्रणोदक (ओज़ोन परत ह्रास का कारण)।\n• DDT (C₁₄H₉Cl₅): कीटनाशक (अब विषाक्तता और दीर्घस्थायित्व के कारण प्रतिबंधित)।"
                    }
                }
            ]
        }
    ]
},
# ============================================
# CHAPTER 7: ALCOHOLS, PHENOLS AND ETHERS
# ============================================
{
    "id": "chapter7",
    "display_name": {
        "english": "CHAPTER 7: ALCOHOLS, PHENOLS AND ETHERS",
        "hindi": "अध्याय 7: एल्कोहॉल, फिनॉल एवं ईथर"
    },
    "color": "#138808",
    "topics": [
        {
            "id": "topic7_1",
            "display_name": {
                "english": "CLASSIFICATION AND NOMENCLATURE",
                "hindi": "वर्गीकरण एवं नामकरण"
            },
            "article_range": "Sections 7.1-7.2",
            "concepts": [
                {
                    "id": "concept7_1_1",
                    "display_name": {
                        "english": "Classification",
                        "hindi": "वर्गीकरण"
                    },
                    "description": {
                        "english": "• Alcohols: Mono, di, tri or polyhydric (based on -OH groups).\n• Based on carbon type: Primary (1°), Secondary (2°), Tertiary (3°), Allylic, Benzylic.\n• Phenols: Mono, di, trihydric (based on -OH groups on benzene).\n• Ethers: Symmetrical (R-O-R), Unsymmetrical (R-O-R').",
                        "hindi": "• एल्कोहॉल: मोनो, डाइ, ट्राइ या पॉलीहाइड्रिक (-OH समूहों के आधार पर)।\n• कार्बन प्रकार के आधार पर: प्राथमिक (1°), द्वितीयक (2°), तृतीयक (3°), एलिलिक, बेंजिलिक।\n• फिनॉल: मोनो, डाइ, ट्राइहाइड्रिक (बेंजीन पर -OH समूहों के आधार पर)।\n• ईथर: सममित (R-O-R), असममित (R-O-R')."
                    }
                },
                {
                    "id": "concept7_1_2",
                    "display_name": {
                        "english": "Nomenclature",
                        "hindi": "नामकरण"
                    },
                    "description": {
                        "english": "• Alcohols: Common name (Alkyl alcohol); IUPAC: replace 'e' of alkane with 'ol' (e.g., Propan-1-ol).\n• Phenols: Hydroxybenzene; substituted phenols use o, m, p or numbers.\n• Ethers: Common name (Alkyl alkyl ether); IUPAC: Alkoxyalkane (larger group as parent).",
                        "hindi": "• एल्कोहॉल: साधारण नाम (एल्किल एल्कोहॉल); IUPAC: एल्केन का 'e' हटाकर 'ol' लगाएं (जैसे, प्रोपेन-1-ऑल)।\n• फिनॉल: हाइड्रॉक्सीबेंजीन; प्रतिस्थापित फिनॉल के लिए o, m, p या संख्याओं का प्रयोग।\n• ईथर: साधारण नाम (एल्किल एल्किल ईथर); IUPAC: एल्कॉक्सीएल्केन (बड़ा समूह जनक के रूप में)।"
                    }
                }
            ]
        },
        {
            "id": "topic7_2",
            "display_name": {
                "english": "PREPARATION",
                "hindi": "विधियाँ"
            },
            "article_range": "Sections 7.4.1-7.4.2, 7.6.1",
            "concepts": [
                {
                    "id": "concept7_2_1",
                    "display_name": {
                        "english": "Preparation of Alcohols",
                        "hindi": "एल्कोहॉलों की विधियाँ"
                    },
                    "description": {
                        "english": "• Hydration of alkenes: Acid catalysed (Markovnikov addition).\n• Hydroboration-oxidation: Diborane (BH₃)₂ then H₂O₂/OH⁻ (Anti-Markovnikov addition).\n• Reduction of carbonyls: RCHO → 1° alcohol; RCOR' → 2° alcohol (NaBH₄ or LiAlH₄).\n• Reduction of carboxylic acids/esters: LiAlH₄ or catalytic hydrogenation of ester.\n• From Grignard reagents: R-MgX + HCHO → 1° alcohol; + other aldehydes → 2° alcohol; + ketones → 3° alcohol.",
                        "hindi": "• एल्कीनों का जलयोजन: अम्ल उत्प्रेरित (मार्कोवनिकोव योग)।\n• हाइड्रोबोरेशन-ऑक्सीकरण: डाइबोरेन (BH₃)₂ फिर H₂O₂/OH⁻ (एंटी-मार्कोवनिकोव योग)।\n• कार्बोनिलों का अपचयन: RCHO → 1° एल्कोहॉल; RCOR' → 2° एल्कोहॉल (NaBH₄ या LiAlH₄).\n• कार्बोक्सिलिक अम्ल/एस्टर का अपचयन: LiAlH₄ या एस्टर का उत्प्रेरक हाइड्रोजनीकरण।\n• ग्रिगनार्ड अभिकर्मक से: R-MgX + HCHO → 1° एल्कोहॉल; + अन्य एल्डिहाइड → 2° एल्कोहॉल; + कीटोन → 3° एल्कोहॉल।"
                    }
                },
                {
                    "id": "concept7_2_2",
                    "display_name": {
                        "english": "Preparation of Phenols",
                        "hindi": "फिनॉल की विधियाँ"
                    },
                    "description": {
                        "english": "• From haloarenes: C₆H₅Cl + NaOH (623K, 300 atm) → C₆H₅ONa → C₆H₅OH (acidification).\n• From benzene sulphonic acid: C₆H₅SO₃H + NaOH (fusion) → C₆H₅ONa → C₆H₅OH.\n• From diazonium salts: C₆H₅N₂⁺Cl⁻ + H₂O (warm) → C₆H₅OH + N₂ + HCl.\n• From cumene (isopropylbenzene): Cumene + O₂ → cumene hydroperoxide → phenol + acetone.",
                        "hindi": "• हैलोऐरीन से: C₆H₅Cl + NaOH (623K, 300 atm) → C₆H₅ONa → C₆H₅OH (अम्लीकरण)।\n• बेंजीन सल्फोनिक अम्ल से: C₆H₅SO₃H + NaOH (संगलन) → C₆H₅ONa → C₆H₅OH.\n• डाइऐज़ोनियम लवणों से: C₆H₅N₂⁺Cl⁻ + H₂O (गर्म) → C₆H₅OH + N₂ + HCl.\n• क्यूमीन (आइसोप्रोपिलबेंजीन) से: क्यूमीन + O₂ → क्यूमीन हाइड्रोपरॉक्साइड → फिनॉल + एसीटोन।"
                    }
                },
                {
                    "id": "concept7_2_3",
                    "display_name": {
                        "english": "Preparation of Ethers",
                        "hindi": "ईथरों की विधियाँ"
                    },
                    "description": {
                        "english": "• Williamson synthesis: R-ONa + R'-X → R-O-R' + NaX (SN2 reaction). Best for primary alkyl halides. Secondary/tertiary halides give elimination products.\n• Dehydration of alcohols: 2ROH (conc. H₂SO₄, 413K) → R-O-R + H₂O. Suitable only for primary alcohols.",
                        "hindi": "• विलियमसन संश्लेषण: R-ONa + R'-X → R-O-R' + NaX (SN2 अभिक्रिया)। प्राथमिक एल्किल हैलाइड के लिए सर्वोत्तम। द्वितीयक/तृतीयक हैलाइड विलोपन उत्पाद देते हैं।\n• एल्कोहॉलों का निर्जलीकरण: 2ROH (सांद्र H₂SO₄, 413K) → R-O-R + H₂O। केवल प्राथमिक एल्कोहॉल के लिए उपयुक्त।"
                    }
                }
            ]
        },
        {
            "id": "topic7_3",
            "display_name": {
                "english": "PHYSICAL PROPERTIES",
                "hindi": "भौतिक गुण"
            },
            "article_range": "Section 7.4.3, 7.6.2",
            "concepts": [
                {
                    "id": "concept7_3_1",
                    "display_name": {
                        "english": "Boiling Points",
                        "hindi": "क्वथनांक"
                    },
                    "description": {
                        "english": "• Alcohols and phenols have high boiling points due to intermolecular H-bonding.\n• Boiling point order: 1° alcohols > 2° alcohols > 3° alcohols (decreasing surface area).\n• Ethers have much lower boiling points than alcohols (no H-bonding), similar to alkanes.",
                        "hindi": "• एल्कोहॉल एवं फिनॉल के क्वथनांक उच्च होते हैं अंतराअणुक H-बंध के कारण।\n• क्वथनांक क्रम: 1° एल्कोहॉल > 2° एल्कोहॉल > 3° एल्कोहॉल (घटते पृष्ठ क्षेत्रफल के साथ)।\n• ईथरों के क्वथनांक एल्कोहॉलों से बहुत कम होते हैं (H-बंध का अभाव), एल्केनों के समान।"
                    }
                },
                {
                    "id": "concept7_3_2",
                    "display_name": {
                        "english": "Solubility",
                        "hindi": "विलेयता"
                    },
                    "description": {
                        "english": "• Lower alcohols and phenols are soluble in water due to H-bonding with water. Solubility decreases with increase in size of alkyl/aryl group.\n• Ethers are slightly soluble in water (H-bond acceptor) but less than alcohols.",
                        "hindi": "• निम्न एल्कोहॉल एवं फिनॉल जल के साथ H-बंध बनाने के कारण जल में विलेय होते हैं। एल्किल/एरिल समूह के आकार बढ़ने के साथ विलेयता घटती है।\n• ईथर जल में अल्प विलेय होते हैं (H-बंध ग्राही) लेकिन एल्कोहॉल से कम।"
                    }
                }
            ]
        },
        
    {
            "id": "topic7_4",
            "display_name": {
                "english": "CHEMICAL REACTIONS OF ALCOHOLS AND PHENOLS",
                "hindi": "एल्कोहॉल एवं फिनॉल की रासायनिक अभिक्रियाएं"
            },
            "article_range": "Section 7.4.4",
            "concepts": [
                {
                    "id": "concept7_4_1",
                    "display_name": {
                        "english": "Acidity of Alcohols and Phenols",
                        "hindi": "एल्कोहॉल एवं फिनॉल की अम्लता"
                    },
                    "description": {
                        "english": "• Phenols are more acidic than alcohols (phenoxide ion stabilized by resonance).\n• Alcohols: Acid strength decreases with electron-donating groups.\n• Phenols: Electron-withdrawing groups (NO₂) increase acidity; electron-donating groups (CH₃) decrease acidity.\n• pKa values: Phenol (10), Ethanol (15.9), Picric acid (0.38).\n• Reaction with metals: 2ROH + 2Na → 2RONa + H₂; 2C₆H₅OH + 2Na → 2C₆H₅ONa + H₂\n• Phenols also react with NaOH: C₆H₅OH + NaOH → C₆H₅ONa + H₂O",
                        "hindi": "• फिनॉल, एल्कोहॉल से अधिक अम्लीय होते हैं (फिनॉक्साइड आयन अनुनाद द्वारा स्थायी होता है)।\n• एल्कोहॉल: इलेक्ट्रॉनदायी समूहों के साथ अम्ल सामर्थ्य घटती है।\n• फिनॉल: इलेक्ट्रॉनअपनेही समूह (NO₂) अम्लता बढ़ाते हैं; इलेक्ट्रॉनदायी समूह (CH₃) अम्लता घटाते हैं।\n• pKa मान: फिनॉल (10), एथेनॉल (15.9), पिक्रिक अम्ल (0.38).\n• धातुओं के साथ अभिक्रिया: 2ROH + 2Na → 2RONa + H₂; 2C₆H₅OH + 2Na → 2C₆H₅ONa + H₂\n• फिनॉल NaOH के साथ भी अभिक्रिया करते हैं: C₆H₅OH + NaOH → C₆H₅ONa + H₂O"
                    }
                },
                {
                    "id": "concept7_4_2",
                    "display_name": {
                        "english": "Esterification",
                        "hindi": "एस्टरीकरण"
                    },
                    "description": {
                        "english": "• R-OH + R'-COOH (H⁺) → R'-COO-R + H₂O\n• R-OH + R'-COCl (pyridine) → R'-COO-R + HCl\n• Acetylation of phenols: C₆H₅OH + (CH₃CO)₂O → C₆H₅OCOCH₃ + CH₃COOH",
                        "hindi": "• R-OH + R'-COOH (H⁺) → R'-COO-R + H₂O\n• R-OH + R'-COCl (पिरिडीन) → R'-COO-R + HCl\n• फिनॉल का एसिटिलीकरण: C₆H₅OH + (CH₃CO)₂O → C₆H₅OCOCH₃ + CH₃COOH"
                    }
                },
                {
                    "id": "concept7_4_3",
                    "display_name": {
                        "english": "Reactions Involving C-O Bond Cleavage",
                        "hindi": "C-O बंध विदलन से संबंधित अभिक्रियाएं"
                    },
                    "description": {
                        "english": "• Reaction with HX: R-OH + HX → R-X + H₂O. Reactivity: 3° > 2° > 1°.\n• Lucas test: ZnCl₂ + conc. HCl distinguishes 1°, 2°, 3° alcohols (turbidity appears immediately for 3°).\n• Reaction with PX₃: 3R-OH + PBr₃ → 3R-Br + H₃PO₃\n• Dehydration: R-OH (conc. H₂SO₄, 443K) → Alkene + H₂O. Ease: 3° > 2° > 1°.\n• Dehydrogenation: 1° alcohol (Cu, 573K) → Aldehyde; 2° alcohol → Ketone; 3° alcohol → Alkene.",
                        "hindi": "• HX के साथ अभिक्रिया: R-OH + HX → R-X + H₂O. अभिक्रियाशीलता: 3° > 2° > 1°.\n• ल्यूकास परीक्षण: ZnCl₂ + सांद्र HCl, 1°, 2°, 3° एल्कोहॉल में अंतर करता है (3° के लिए तुरंत मैलापन)।\n• PX₃ के साथ अभिक्रिया: 3R-OH + PBr₃ → 3R-Br + H₃PO₃\n• निर्जलीकरण: R-OH (सांद्र H₂SO₄, 443K) → एल्कीन + H₂O. सरलता क्रम: 3° > 2° > 1°.\n• डिहाइड्रोजनीकरण: 1° एल्कोहॉल (Cu, 573K) → एल्डिहाइड; 2° एल्कोहॉल → कीटोन; 3° एल्कोहॉल → एल्कीन।"
                    }
                },
                {
                    "id": "concept7_4_4",
                    "display_name": {
                        "english": "Oxidation of Alcohols",
                        "hindi": "एल्कोहॉलों का ऑक्सीकरण"
                    },
                    "description": {
                        "english": "• 1° alcohol [O] → Aldehyde [O] → Carboxylic acid.\n• PCC (Pyridinium chlorochromate) stops at aldehyde stage.\n• 2° alcohol [O] → Ketone.\n• 3° alcohols resistant to oxidation; under strong conditions undergo C-C cleavage.",
                        "hindi": "• 1° एल्कोहॉल [O] → एल्डिहाइड [O] → कार्बोक्सिलिक अम्ल।\n• PCC (पिरिडीनियम क्लोरोक्रोमेट) एल्डिहाइड अवस्था पर रोक देता है।\n• 2° एल्कोहॉल [O] → कीटोन।\n• 3° एल्कोहॉल ऑक्सीकरण के प्रति प्रतिरोधी; प्रबल परिस्थितियों में C-C विदलन होता है।"
                    }
                },
                {
                    "id": "concept7_4_5",
                    "display_name": {
                        "english": "Electrophilic Substitution of Phenols",
                        "hindi": "फिनॉल का इलेक्ट्रॉनस्नेही प्रतिस्थापन"
                    },
                    "description": {
                        "english": "• -OH group is o,p-directing and activates the ring.\n• Nitration: Dilute HNO₃ gives o- and p-nitrophenol; conc. HNO₃ gives picric acid (2,4,6-trinitrophenol).\n• Halogenation: With Br₂ water gives 2,4,6-tribromophenol (white precipitate). In CS₂/CHCl₃ gives monobromophenols.\n• Kolbe's reaction: C₆H₅ONa + CO₂ (then H⁺) → Salicylic acid (o-hydroxybenzoic acid).\n• Reimer-Tiemann reaction: C₆H₅OH + CHCl₃ + NaOH → Salicylaldehyde (o-hydroxybenzaldehyde).",
                        "hindi": "• -OH समूह o,p-निर्देशक होता है और वलय को सक्रिय करता है।\n• नाइट्रीकरण: तनु HNO₃ o- और p-नाइट्रोफिनॉल देता है; सांद्र HNO₃ पिक्रिक अम्ल (2,4,6-ट्राइनाइट्रोफिनॉल) देता है।\n• हैलोजनीकरण: Br₂ जल के साथ 2,4,6-ट्राइब्रोमोफिनॉल (श्वेत अवक्षेप) देता है। CS₂/CHCl₃ में मोनोब्रोमोफिनॉल देता है।\n• कोल्बे अभिक्रिया: C₆H₅ONa + CO₂ (फिर H⁺) → सैलिसिलिक अम्ल (o-हाइड्रॉक्सीबेन्जोइक अम्ल)।\n• राइमर-टीमैन अभिक्रिया: C₆H₅OH + CHCl₃ + NaOH → सैलिसिलैल्डिहाइड (o-हाइड्रॉक्सीबेन्जैल्डिहाइड)।"
                    }
                }
            ]
        },
        {
            "id": "topic7_5",
            "display_name": {
                "english": "CHEMICAL REACTIONS OF ETHERS",
                "hindi": "ईथरों की रासायनिक अभिक्रियाएं"
            },
            "article_range": "Section 7.6.3",
            "concepts": [
                {
                    "id": "concept7_5_1",
                    "display_name": {
                        "english": "Cleavage of C-O Bond",
                        "hindi": "C-O बंध का विदलन"
                    },
                    "description": {
                        "english": "• R-O-R' + HI (excess, heat) → R-I + R'-I (for dialkyl ethers).\n• Reactivity order: HI > HBr > HCl.\n• Mechanism: Protonation of ether, then SN2 attack by I⁻ on less hindered alkyl group (for primary/secondary). For tertiary alkyl, SN1 pathway.\n• Alkyl aryl ethers: C₆H₅-O-CH₃ + HI → C₆H₅-OH + CH₃-I (O-CH₃ bond cleaved due to more stable C₆H₅-O bond).",
                        "hindi": "• R-O-R' + HI (आधिक्य, गर्म) → R-I + R'-I (डाइएल्किल ईथर के लिए)।\n• अभिक्रियाशीलता क्रम: HI > HBr > HCl.\n• क्रियाविधि: ईथर का प्रोटॉनीकरण, फिर कम अवरोधित एल्किल समूह पर I⁻ का SN2 आक्रमण (प्राथमिक/द्वितीयक के लिए)। तृतीयक एल्किल के लिए, SN1 मार्ग।\n• एल्किल एरिल ईथर: C₆H₅-O-CH₃ + HI → C₆H₅-OH + CH₃-I (O-CH₃ बंध टूटता है क्योंकि C₆H₅-O बंध अधिक स्थायी है)।"
                    }
                },
                {
                    "id": "concept7_5_2",
                    "display_name": {
                        "english": "Electrophilic Substitution of Aryl Ethers",
                        "hindi": "एरिल ईथरों का इलेक्ट्रॉनस्नेही प्रतिस्थापन"
                    },
                    "description": {
                        "english": "• -OR group is o,p-directing and activates the ring.\n• Halogenation: Anisole with Br₂ in ethanoic acid gives p-bromoanisole (90%).\n• Nitration: Anisole with HNO₃/H₂SO₄ gives o- and p-nitroanisole.\n• Friedel-Crafts: Anisole with R-Cl/AlCl₃ gives o- and p-alkyl anisoles.",
                        "hindi": "• -OR समूह o,p-निर्देशक होता है और वलय को सक्रिय करता है।\n• हैलोजनीकरण: एनिसॉल का Br₂ के साथ एथेनोइक अम्ल में p-ब्रोमोएनिसॉल देता है (90%)।\n• नाइट्रीकरण: एनिसॉल का HNO₃/H₂SO₄ के साथ o- और p-नाइट्रोएनिसॉल देता है।\n• फ्रीडेल-क्राफ्ट्स: एनिसॉल का R-Cl/AlCl₃ के साथ o- और p-एल्किल एनिसॉल देता है।"
                    }
                }
            ]
        },
        {
            "id": "topic7_6",
            "display_name": {
                "english": "COMMERCIALLY IMPORTANT ALCOHOLS",
                "hindi": "व्यापारिक रूप से महत्वपूर्ण एल्कोहॉल"
            },
            "article_range": "Section 7.5",
            "concepts": [
                {
                    "id": "concept7_6_1",
                    "display_name": {
                        "english": "Methanol and Ethanol",
                        "hindi": "मेथनॉल एवं एथेनॉल"
                    },
                    "description": {
                        "english": "• Methanol (CH₃OH): 'Wood spirit'. Manufactured by catalytic hydrogenation of CO (ZnO-Cr₂O₃, 200-300 atm). Poisonous, causes blindness. Used as solvent, for making formaldehyde.\n• Ethanol (C₂H₅OH): Produced by fermentation of sugars (enzymes invertase and zymase from yeast). Also by hydration of ethene. Used as solvent, in beverages. Denatured with CuSO₄ and pyridine.",
                        "hindi": "• मेथनॉल (CH₃OH): 'वुड स्पिरिट'। CO के उत्प्रेरक हाइड्रोजनीकरण द्वारा निर्मित (ZnO-Cr₂O₃, 200-300 atm)। विषैला, अंधापन पैदा करता है। विलायक के रूप में, फॉर्मेल्डिहाइड बनाने में प्रयुक्त।\n• एथेनॉल (C₂H₅OH): शर्करा के किण्वन द्वारा (यीस्ट से एंजाइम इन्वर्टेज और जाइमेज) निर्मित। एथीन के जलयोजन द्वारा भी। विलायक के रूप में, पेय पदार्थों में प्रयुक्त। CuSO₄ और पिरिडीन मिलाकर विरूपित किया जाता है।"
                    }
                }
            ]
        }
        ]
    },

    {
    "id": "chapter8",
    "display_name": {
        "english": "CHAPTER 8: ALDEHYDES, KETONES AND CARBOXYLIC ACIDS",
        "hindi": "अध्याय 8: एल्डिहाइड, कीटोन एवं कार्बोक्सिलिक अम्ल"
    },
    "color": "#FFD700",
    "topics": [
        {
            "id": "topic8_1",
            "display_name": {
                "english": "NOMENCLATURE AND STRUCTURE",
                "hindi": "नामकरण एवं संरचना"
            },
            "article_range": "Sections 8.1-8.1.2",
            "concepts": [
                {
                    "id": "concept8_1_1",
                    "display_name": {
                        "english": "Nomenclature",
                        "hindi": "नामकरण"
                    },
                    "description": {
                        "english": "• Aldehydes: Common name (from carboxylic acid, -ic acid → -aldehyde); IUPAC: replace 'e' of alkane with 'al'.\n• Ketones: Common name (alkyl alkyl ketone); IUPAC: replace 'e' of alkane with 'one'.\n• Aromatic aldehydes: Benzaldehyde (common and IUPAC accepted).",
                        "hindi": "• एल्डिहाइड: साधारण नाम (कार्बोक्सिलिक अम्ल से, -ic acid → -aldehyde); IUPAC: एल्केन का 'e' हटाकर 'al' लगाएं।\n• कीटोन: साधारण नाम (एल्किल एल्किल कीटोन); IUPAC: एल्केन का 'e' हटाकर 'one' लगाएं।\n• एरोमैटिक एल्डिहाइड: बेंजैल्डिहाइड (साधारण एवं IUPAC स्वीकृत)।"
                    }
                },
                {
                    "id": "concept8_1_2",
                    "display_name": {
                        "english": "Structure of Carbonyl Group",
                        "hindi": "कार्बोनिल समूह की संरचना"
                    },
                    "description": {
                        "english": "• C=O bond: sp² hybridised carbon, trigonal planar (~120° bond angles).\n• σ bond (sp²-sp² overlap) and π bond (p-p overlap).\n• Polarised due to electronegativity of oxygen (C δ+, O δ-).\n• Resonance: contributes to polarity.",
                        "hindi": "• C=O बंध: sp² संकरित कार्बन, त्रिकोणीय समतल (~120° बंध कोण)।\n• σ बंध (sp²-sp² अतिव्यापन) एवं π बंध (p-p अतिव्यापन)।\n• ऑक्सीजन की वैद्युतऋणात्मकता के कारण ध्रुवित (C δ+, O δ-).\n• अनुनाद: ध्रुवता में योगदान करता है।"
                    }
                }
            ]
        },
        {
            "id": "topic8_2",
            "display_name": {
                "english": "PREPARATION OF ALDEHYDES AND KETONES",
                "hindi": "एल्डिहाइड एवं कीटोन की विधियाँ"
            },
            "article_range": "Sections 8.2",
            "concepts": [
                {
                    "id": "concept8_2_1",
                    "display_name": {
                        "english": "Preparation of Aldehydes",
                        "hindi": "एल्डिहाइड की विधियाँ"
                    },
                    "description": {
                        "english": "• Oxidation of 1° alcohols: PCC stops at aldehyde.\n• Dehydrogenation of 1° alcohols: Cu, 573K.\n• Rosenmund reduction: RCOCl + H₂ (Pd/BaSO₄) → RCHO + HCl.\n• Stephen reaction: RCN + SnCl₂/HCl → RCH=NH → RCHO (hydrolysis).\n• Reduction with DIBAL-H: RCN or RCOOR' → RCHO.\n• Etard reaction: Toluene + CrO₂Cl₂ → complex → Benzaldehyde.\n• Gatterman-Koch reaction: C₆H₆ + CO + HCl (AlCl₃/CuCl) → C₆H₅CHO.",
                        "hindi": "• 1° एल्कोहॉल का ऑक्सीकरण: PCC एल्डिहाइड पर रोक देता है।\n• 1° एल्कोहॉल का डिहाइड्रोजनीकरण: Cu, 573K.\n• रोजेनमुंड अपचयन: RCOCl + H₂ (Pd/BaSO₄) → RCHO + HCl.\n• स्टीफन अभिक्रिया: RCN + SnCl₂/HCl → RCH=NH → RCHO (जल अपघटन)।\n• DIBAL-H से अपचयन: RCN या RCOOR' → RCHO.\n• एटार्ड अभिक्रिया: टॉलूईन + CrO₂Cl₂ → संकुल → बेंजैल्डिहाइड।\n• गैटरमान-कोच अभिक्रिया: C₆H₆ + CO + HCl (AlCl₃/CuCl) → C₆H₅CHO."
                    }
                },
                {
                    "id": "concept8_2_2",
                    "display_name": {
                        "english": "Preparation of Ketones",
                        "hindi": "कीटोन की विधियाँ"
                    },
                    "description": {
                        "english": "• Oxidation of 2° alcohols.\n• Dehydrogenation of 2° alcohols: Cu, 573K.\n• From acyl chlorides and dialkylcadmium: 2R'COCl + R₂Cd → 2R'COR + CdCl₂.\n• From nitriles: RCN + R'MgX → imine complex → RCOR'.\n• Friedel-Crafts acylation: C₆H₆ + RCOCl (AlCl₃) → C₆H₅COR.\n• Ozonolysis of alkenes gives aldehydes or ketones depending on substitution.",
                        "hindi": "• 2° एल्कोहॉल का ऑक्सीकरण।\n• 2° एल्कोहॉल का डिहाइड्रोजनीकरण: Cu, 573K.\n• एसिल क्लोराइड एवं डाइएल्किलकैडमियम से: 2R'COCl + R₂Cd → 2R'COR + CdCl₂.\n• नाइट्राइल से: RCN + R'MgX → इमीन संकुल → RCOR'.\n• फ्रीडेल-क्राफ्ट्स एसिलीकरण: C₆H₆ + RCOCl (AlCl₃) → C₆H₅COR.\n• एल्कीन का ओजोनोलिसिस प्रतिस्थापन के अनुसार एल्डिहाइड या कीटोन देता है।"
                    }
                }
            ]
        },
        {
            "id": "topic8_3",
            "display_name": {
                "english": "PHYSICAL PROPERTIES",
                "hindi": "भौतिक गुण"
            },
            "article_range": "Section 8.3",
            "concepts": [
                {
                    "id": "concept8_3_1",
                    "display_name": {
                        "english": "Boiling Points and Solubility",
                        "hindi": "क्वथनांक एवं विलेयता"
                    },
                    "description": {
                        "english": "• Higher boiling points than hydrocarbons/ethers (dipole-dipole interactions), lower than alcohols (no H-bonding).\n• Lower aldehydes/ketones miscible with water (H-bond acceptors). Solubility decreases with chain length.\n• Order: n-Butane < Methoxyethane < Propanal < Acetone < Propan-1-ol (boiling point).",
                        "hindi": "• हाइड्रोकार्बन/ईथर से उच्च क्वथनांक (द्विध्रुव-द्विध्रुव अन्योन्य क्रियाएं), एल्कोहॉल से कम (H-बंध का अभाव)।\n• निम्न एल्डिहाइड/कीटोन जल के साथ मिश्रणीय (H-बंध ग्राही)। श्रृंखला लंबाई बढ़ने के साथ विलेयता घटती है।\n• क्रम: n-ब्यूटेन < मेथॉक्सीएथेन < प्रोपेनल < एसीटोन < प्रोपेन-1-ऑल (क्वथनांक)।"
                    }
                }
            ]
        },
        {
            "id": "topic8_4",
            "display_name": {
                "english": "CHEMICAL REACTIONS OF ALDEHYDES AND KETONES",
                "hindi": "एल्डिहाइड एवं कीटोन की रासायनिक अभिक्रियाएं"
            },
            "article_range": "Section 8.4",
            "concepts": [
                {
                    "id": "concept8_4_1",
                    "display_name": {
                        "english": "Nucleophilic Addition Reactions",
                        "hindi": "नाभिकस्नेही योगात्मक अभिक्रियाएं"
                    },
                    "description": {
                        "english": "• Mechanism: Nucleophile attacks electrophilic carbonyl C, forming tetrahedral intermediate, then protonation.\n• Reactivity: Aldehydes more reactive than ketones (steric and electronic reasons).\n• Addition of HCN: >C=O + HCN → Cyanohydrin (base catalysed).\n• Addition of NaHSO₃: Forms bisulphite addition product (used for separation/purification).\n• Addition of Grignard reagents: → Alcohols.\n• Addition of alcohols: RCHO + R'OH (dry HCl) → Hemiacetal + R'OH → Acetal (gem-dialkoxy). Ketones give ketals with ethylene glycol.\n• Addition of ammonia derivatives: >C=O + H₂N-Z → >C=N-Z + H₂O (oximes, hydrazones, semicarbazones, etc.)",
                        "hindi": "• क्रियाविधि: नाभिकस्नेही इलेक्ट्रॉनस्नेही कार्बोनिल C पर आक्रमण करता है, चतुष्फलकीय माध्यमिक बनाता है, फिर प्रोटॉनीकरण।\n• अभिक्रियाशीलता: एल्डिहाइड कीटोन से अधिक अभिक्रियाशील (स्टेरिक एवं इलेक्ट्रॉनिक कारण)।\n• HCN का योग: >C=O + HCN → सायनोहाइड्रिन (क्षार उत्प्रेरित)।\n• NaHSO₃ का योग: बाइसल्फाइट योग उत्पाद बनाता है (पृथक्करण/शोधन के लिए प्रयुक्त)।\n• ग्रिगनार्ड अभिकर्मकों का योग: → एल्कोहॉल।\n• एल्कोहॉल का योग: RCHO + R'OH (शुष्क HCl) → हेमिएसिटल + R'OH → एसिटल (जेम-डाइएल्कॉक्सी)। कीटोन एथिलीन ग्लाइकॉल के साथ कीटल देते हैं।\n• अमोनिया व्युत्पन्नों का योग: >C=O + H₂N-Z → >C=N-Z + H₂O (ऑक्सीम, हाइड्राजोन, सेमीकार्बाजोन, आदि)।"
                    }
                },
                {
                    "id": "concept8_4_2",
                    "display_name": {
                        "english": "Reduction Reactions",
                        "hindi": "अपचयन अभिक्रियाएं"
                    },
                    "description": {
                        "english": "• To alcohols: NaBH₄ or LiAlH₄ or catalytic hydrogenation (RCHO → 1° alcohol; RCOR' → 2° alcohol).\n• To hydrocarbons (Clemmensen reduction): >C=O + Zn-Hg/HCl → -CH₂- (for acid-sensitive compounds).\n• To hydrocarbons (Wolff-Kishner reduction): >C=O + NH₂NH₂, then KOH/ethylene glycol, heat → -CH₂-.",
                        "hindi": "• एल्कोहॉल में: NaBH₄ या LiAlH₄ या उत्प्रेरक हाइड्रोजनीकरण (RCHO → 1° एल्कोहॉल; RCOR' → 2° एल्कोहॉल)।\n• हाइड्रोकार्बन में (क्लीमेन्सन अपचयन): >C=O + Zn-Hg/HCl → -CH₂- (अम्ल-सुग्राही यौगिकों के लिए)।\n• हाइड्रोकार्बन में (वुल्फ-किश्नर अपचयन): >C=O + NH₂NH₂, फिर KOH/एथिलीन ग्लाइकॉल, गर्म → -CH₂-."
                    }
                },
                {
                    "id": "concept8_4_3",
                    "display_name": {
                        "english": "Oxidation Reactions",
                        "hindi": "ऑक्सीकरण अभिक्रियाएं"
                    },
                    "description": {
                        "english": "• Aldehydes easily oxidised to carboxylic acids (even by mild oxidising agents).\n• Ketones undergo C-C cleavage under vigorous conditions, giving mixture of acids.\n• Tollens' test (ammoniacal AgNO₃): RCHO → RCOO⁻ + Ag mirror. Ketones do not react.\n• Fehling's test (Cu²⁺ complex): RCHO → Cu₂O (red-brown ppt). Aromatic aldehydes do not react.\n• Iodoform test: Methyl ketones (CH₃COR) and CH₃CH(OH)-R give yellow ppt of CHI₃ with I₂/NaOH.",
                        "hindi": "• एल्डिहाइड सरलता से कार्बोक्सिलिक अम्ल में ऑक्सीकृत हो जाते हैं (हल्के ऑक्सीकारकों द्वारा भी)।\n• कीटोन प्रबल परिस्थितियों में C-C विदलन से गुजरते हैं, अम्लों का मिश्रण देते हैं।\n• टॉलेन परीक्षण (अमोनियाकल AgNO₃): RCHO → RCOO⁻ + Ag दर्पण। कीटोन अभिक्रिया नहीं करते।\n• फेहलिंग परीक्षण (Cu²⁺ संकुल): RCHO → Cu₂O (लाल-भूरा अवक्षेप)। एरोमैटिक एल्डिहाइड अभिक्रिया नहीं करते।\n• आयोडोफॉर्म परीक्षण: मेथिल कीटोन (CH₃COR) एवं CH₃CH(OH)-R, I₂/NaOH के साथ CHI₃ का पीला अवक्षेप देते हैं।"
                    }
                },
                {
                    "id": "concept8_4_4",
                    "display_name": {
                        "english": "Reactions due to α-Hydrogen",
                        "hindi": "α-हाइड्रोजन के कारण अभिक्रियाएं"
                    },
                    "description": {
                        "english": "• Acidity of α-H: Due to resonance stabilisation of enolate ion.\n• Aldol condensation: Two molecules of aldehyde/ketone with α-H in presence of dilute alkali give β-hydroxy aldehyde/ketone (aldol/ketol) which on heating gives α,β-unsaturated carbonyl compound.\n• Cross aldol: Between two different carbonyl compounds (can give mixture of products).",
                        "hindi": "• α-H की अम्लता: एनोलेट आयन के अनुनाद स्थायीकरण के कारण।\n• एल्डोल संघनन: α-H वाले एल्डिहाइड/कीटोन के दो अणु तनु क्षार की उपस्थिति में β-हाइड्रॉक्सी एल्डिहाइड/कीटोन (एल्डोल/कीटोल) देते हैं जो गर्म करने पर α,β-असंतृप्त कार्बोनिल यौगिक देता है।\n• क्रॉस एल्डोल: दो भिन्न कार्बोनिल यौगिकों के बीच (उत्पादों का मिश्रण दे सकता है)।"
                    }
                },
                {
                    "id": "concept8_4_5",
                    "display_name": {
                        "english": "Cannizzaro Reaction",
                        "hindi": "कैनिजारो अभिक्रिया"
                    },
                    "description": {
                        "english": "• Aldehydes without α-H (e.g., HCHO, C₆H₅CHO) undergo self oxidation-reduction with conc. alkali.\n• 2HCHO + conc. NaOH → CH₃OH (reduced) + HCOONa (oxidised).",
                        "hindi": "• α-H रहित एल्डिहाइड (जैसे, HCHO, C₆H₅CHO) सांद्र क्षार के साथ स्व-ऑक्सीकरण-अपचयन से गुजरते हैं।\n• 2HCHO + सांद्र NaOH → CH₃OH (अपचयित) + HCOONa (ऑक्सीकृत)।"
                    }
                }
            ]
        },
        {
            "id": "topic8_5",
            "display_name": {
                "english": "CARBOXYLIC ACIDS",
                "hindi": "कार्बोक्सिलिक अम्ल"
            },
            "article_range": "Sections 8.6-8.10",
            "concepts": [
                {
                    "id": "concept8_5_1",
                    "display_name": {
                        "english": "Nomenclature and Structure",
                        "hindi": "नामकरण एवं संरचना"
                    },
                    "description": {
                        "english": "• Common names: Formic acid (HCOOH), Acetic acid (CH₃COOH), etc.\n• IUPAC: Replace 'e' of alkane with 'oic acid'.\n• Structure: Carboxyl carbon sp² hybridised, planar. Resonance stabilised: -COOH group has partial double bond character.",
                        "hindi": "• साधारण नाम: फॉर्मिक अम्ल (HCOOH), एसिटिक अम्ल (CH₃COOH), आदि।\n• IUPAC: एल्केन का 'e' हटाकर 'ओइक अम्ल' लगाएं।\n• संरचना: कार्बोक्सिल कार्बन sp² संकरित, समतलीय। अनुनाद द्वारा स्थायीकृत: -COOH समूह में आंशिक द्विबंध लक्षण।"
                    }
                },
                {
                    "id": "concept8_5_2",
                    "display_name": {
                        "english": "Preparation of Carboxylic Acids",
                        "hindi": "कार्बोक्सिलिक अम्ल की विधियाँ"
                    },
                    "description": {
                        "english": "• Oxidation of 1° alcohols and aldehydes (KMnO₄, K₂Cr₂O₇).\n• Oxidation of alkyl benzenes: C₆H₅-R [O] → C₆H₅COOH (side chain oxidation).\n• Hydrolysis of nitriles: RCN + H₂O (H⁺/OH⁻) → RCOOH.\n• From Grignard reagents: RMgX + CO₂ (dry ice) → RCOOMgX → RCOOH.\n• Hydrolysis of acyl halides, anhydrides, esters.",
                        "hindi": "• 1° एल्कोहॉल एवं एल्डिहाइड का ऑक्सीकरण (KMnO₄, K₂Cr₂O₇).\n• एल्किल बेंजीन का ऑक्सीकरण: C₆H₅-R [O] → C₆H₅COOH (पार्श्व श्रृंखला ऑक्सीकरण)।\n• नाइट्राइल का जल अपघटन: RCN + H₂O (H⁺/OH⁻) → RCOOH.\n• ग्रिगनार्ड अभिकर्मकों से: RMgX + CO₂ (शुष्क बर्फ) → RCOOMgX → RCOOH.\n• एसिल हैलाइड, एनहाइड्राइड, एस्टर का जल अपघटन।"
                    }
                },
                {
                    "id": "concept8_5_3",
                    "display_name": {
                        "english": "Acidity and Effect of Substituents",
                        "hindi": "अम्लता एवं प्रतिस्थापियों का प्रभाव"
                    },
                    "description": {
                        "english": "• Carboxylic acids are stronger acids than phenols (carboxylate ion stabilised by two equivalent resonance structures).\n• pKa values: HCOOH (3.75), CH₃COOH (4.76).\n• Electron-withdrawing groups (EWG) increase acidity by stabilising carboxylate ion.\n• Electron-donating groups (EDG) decrease acidity.\n• Inductive effect decreases with distance.",
                        "hindi": "• कार्बोक्सिलिक अम्ल, फिनॉल से प्रबल अम्ल होते हैं (कार्बोक्सिलेट आयन दो समतुल्य अनुनाद संरचनाओं द्वारा स्थायी होता है)।\n• pKa मान: HCOOH (3.75), CH₃COOH (4.76).\n• इलेक्ट्रॉनअपनेही समूह (EWG) कार्बोक्सिलेट आयन को स्थायी करके अम्लता बढ़ाते हैं।\n• इलेक्ट्रॉनदायी समूह (EDG) अम्लता घटाते हैं।\n• प्रेरणिक प्रभाव दूरी के साथ घटता है।"
                    }
                },
                {
                    "id": "concept8_5_4",
                    "display_name": {
                        "english": "Reactions of Carboxylic Acids",
                        "hindi": "कार्बोक्सिलिक अम्ल की अभिक्रियाएं"
                    },
                    "description": {
                        "english": "• Reactions involving O-H cleavage: Salt formation with metals/alkalies/carbonates/bicarbonates.\n• Formation of anhydride: Heating with P₂O₅ or mineral acid.\n• Esterification: RCOOH + R'OH (H⁺) → RCOOR' + H₂O.\n• Reactions with PCl₅, PCl₃, SOCl₂: → RCOCl.\n• Reaction with ammonia: RCOOH + NH₃ → RCOONH₄ → RCONH₂ (amide).\n• Reduction: LiAlH₄ or B₂H₆ → 1° alcohol.\n• Decarboxylation: RCOONa + NaOH (soda lime) → R-H + Na₂CO₃.\n• Hell-Volhard-Zelinsky (HVZ) reaction: α-halogenation with Cl₂/Br₂ in presence of red P.",
                        "hindi": "• O-H विदलन से संबंधित अभिक्रियाएं: धातुओं/क्षारकों/कार्बोनेट/बाइकार्बोनेट के साथ लवण निर्माण।\n• एनहाइड्राइड का निर्माण: P₂O₅ या खनिज अम्ल के साथ गर्म करने पर।\n• एस्टरीकरण: RCOOH + R'OH (H⁺) → RCOOR' + H₂O.\n• PCl₅, PCl₃, SOCl₂ के साथ अभिक्रिया: → RCOCl.\n• अमोनिया के साथ अभिक्रिया: RCOOH + NH₃ → RCOONH₄ → RCONH₂ (एमाइड).\n• अपचयन: LiAlH₄ या B₂H₆ → 1° एल्कोहॉल।\n• डीकार्बोक्सिलीकरण: RCOONa + NaOH (सोडा लाइम) → R-H + Na₂CO₃.\n• हेल-वोल्हार्ड-जेलिंस्की (HVZ) अभिक्रिया: लाल P की उपस्थिति में Cl₂/Br₂ के साथ α-हैलोजनीकरण।"
                    }
                }
            ]
        }
        ]
    },
    {
    "id": "chapter9",
    "display_name": {
        "english": "CHAPTER 9: AMINES",
        "hindi": "अध्याय 9: एमीन"
    },
    "color": "#FF9933",
    "topics": [
        {
            "id": "topic9_1",
            "display_name": {
                "english": "CLASSIFICATION AND NOMENCLATURE",
                "hindi": "वर्गीकरण एवं नामकरण"
            },
            "article_range": "Sections 9.2-9.3",
            "concepts": [
                {
                    "id": "concept9_1_1",
                    "display_name": {
                        "english": "Classification",
                        "hindi": "वर्गीकरण"
                    },
                    "description": {
                        "english": "• Primary (1°): R-NH₂ (one H replaced).\n• Secondary (2°): R₂NH or R-NH-R' (two H replaced).\n• Tertiary (3°): R₃N (three H replaced).\n• Simple amines: Same alkyl/aryl groups. Mixed amines: Different groups.",
                        "hindi": "• प्राथमिक (1°): R-NH₂ (एक H प्रतिस्थापित)।\n• द्वितीयक (2°): R₂NH या R-NH-R' (दो H प्रतिस्थापित)।\n• तृतीयक (3°): R₃N (तीन H प्रतिस्थापित)।\n• सरल एमीन: समान एल्किल/एरिल समूह। मिश्रित एमीन: भिन्न समूह।"
                    }
                },
                {
                    "id": "concept9_1_2",
                    "display_name": {
                        "english": "Nomenclature",
                        "hindi": "नामकरण"
                    },
                    "description": {
                        "english": "• Common name: Alkylamine (e.g., Methylamine).\n• IUPAC: Alkanamine (e.g., Methanamine).\n• Secondary/tertiary: Use 'N' to denote substituents on nitrogen (e.g., N-Methylethanamine).\n• Arylamines: Aniline (C₆H₅NH₂) is accepted IUPAC name.",
                        "hindi": "• साधारण नाम: एल्किलमीन (जैसे, मेथिलमीन)।\n• IUPAC: एल्केनमीन (जैसे, मेथेनमीन)।\n• द्वितीयक/तृतीयक: नाइट्रोजन पर प्रतिस्थापियों को दर्शाने के लिए 'N' का प्रयोग (जैसे, N-मेथिलएथेनमीन)।\n• एरिलमीन: एनिलीन (C₆H₅NH₂) IUPAC नाम के रूप में स्वीकृत है।"
                    }
                }
            ]
        },
        {
            "id": "topic9_2",
            "display_name": {
                "english": "PREPARATION OF AMINES",
                "hindi": "एमीनों की विधियाँ"
            },
            "article_range": "Section 9.4",
            "concepts": [
                {
                    "id": "concept9_2_1",
                    "display_name": {
                        "english": "Reduction of Nitro Compounds",
                        "hindi": "नाइट्रो यौगिकों का अपचयन"
                    },
                    "description": {
                        "english": "• R-NO₂ + H₂ (Ni/Pd/Pt) or Sn/HCl or Fe/HCl → R-NH₂.\n• Fe/HCl is preferred industrially (FeCl₂ formed hydrolyses to release HCl).",
                        "hindi": "• R-NO₂ + H₂ (Ni/Pd/Pt) या Sn/HCl या Fe/HCl → R-NH₂.\n• Fe/HCl औद्योगिक रूप से पसंद किया जाता है (बनने वाला FeCl₂ जल अपघटित होकर HCl मुक्त करता है)।"
                    }
                },
                {
                    "id": "concept9_2_2",
                    "display_name": {
                        "english": "Ammonolysis of Alkyl Halides",
                        "hindi": "एल्किल हैलाइडों का अमोनॉलिसिस"
                    },
                    "description": {
                        "english": "• R-X + NH₃ (ethanol, sealed tube, 373K) → R-NH₂ + HX.\n• Primary amine formed can further react to give secondary, tertiary amines and quaternary ammonium salt.\n• Not a good method to prepare pure primary amines (mixture obtained).",
                        "hindi": "• R-X + NH₃ (एथेनॉल, सीलबंद नली, 373K) → R-NH₂ + HX.\n• बनने वाला प्राथमिक एमीन आगे क्रिया करके द्वितीयक, तृतीयक एमीन एवं चतुष्क अमोनियम लवण दे सकता है।\n• शुद्ध प्राथमिक एमीन बनाने की अच्छी विधि नहीं (मिश्रण मिलता है)।"
                    }
                },
                {
                    "id": "concept9_2_3",
                    "display_name": {
                        "english": "Gabriel Phthalimide Synthesis",
                        "hindi": "गैब्रिएल थैलिमाइड संश्लेषण"
                    },
                    "description": {
                        "english": "• Phthalimide + KOH (ethanol) → Potassium phthalimide + R-X → N-alkylphthalimide + hydrolysis (NaOH) → Primary amine.\n• Gives pure primary amine. Aromatic primary amines cannot be prepared by this method.",
                        "hindi": "• थैलिमाइड + KOH (एथेनॉल) → पोटैशियम थैलिमाइड + R-X → N-एल्किलथैलिमाइड + जल अपघटन (NaOH) → प्राथमिक एमीन।\n• शुद्ध प्राथमिक एमीन देता है। इस विधि द्वारा एरोमैटिक प्राथमिक एमीन नहीं बनाए जा सकते।"
                    }
                },
                {
                    "id": "concept9_2_4",
                    "display_name": {
                        "english": "Hoffmann Bromamide Degradation",
                        "hindi": "हॉफमैन ब्रोमैमाइड अपघटन"
                    },
                    "description": {
                        "english": "• RCONH₂ + Br₂ + 4NaOH → R-NH₂ + 2NaBr + Na₂CO₃ + 2H₂O.\n• The amine formed has one carbon less than the amide.\n• Used for descending the series.",
                        "hindi": "• RCONH₂ + Br₂ + 4NaOH → R-NH₂ + 2NaBr + Na₂CO₃ + 2H₂O.\n• बनने वाला एमीन, एमाइड से एक कार्बन कम होता है।\n• श्रेणी अवरोहण के लिए प्रयुक्त।"
                    }
                }
            ]
        },
        {
            "id": "topic9_3",
            "display_name": {
                "english": "PHYSICAL PROPERTIES",
                "hindi": "भौतिक गुण"
            },
            "article_range": "Section 9.5",
            "concepts": [
                {
                    "id": "concept9_3_1",
                    "display_name": {
                        "english": "Boiling Points and Solubility",
                        "hindi": "क्वथनांक एवं विलेयता"
                    },
                    "description": {
                        "english": "• Lower aliphatic amines are gases with fishy odour.\n• Boiling point order: 1° > 2° > 3° (due to intermolecular H-bonding in 1° and 2°; 3° has no H-bonding).\n• Lower amines soluble in water (H-bonding). Solubility decreases with increase in molar mass.\n• More soluble in organic solvents.",
                        "hindi": "• निम्न एलिफैटिक एमीन गैसें होती हैं जिनमें मछली जैसी गंध होती है।\n• क्वथनांक क्रम: 1° > 2° > 3° (1° एवं 2° में अंतराअणुक H-बंध के कारण; 3° में H-बंध नहीं होता)।\n• निम्न एमीन जल में विलेय (H-बंध)। मोलर द्रव्यमान बढ़ने के साथ विलेयता घटती है।\n• कार्बनिक विलायकों में अधिक विलेय।"
                    }
                }
            ]
        },
        {
            "id": "topic9_4",
            "display_name": {
                "english": "CHEMICAL REACTIONS",
                "hindi": "रासायनिक अभिक्रियाएं"
            },
            "article_range": "Section 9.6",
            "concepts": [
                {
                    "id": "concept9_4_1",
                    "display_name": {
                        "english": "Basic Character of Amines",
                        "hindi": "एमीनों का क्षारकीय लक्षण"
                    },
                    "description": {
                        "english": "• Amines are Lewis bases due to lone pair on N.\n• R-NH₂ + H₂O ⇌ R-NH₃⁺ + OH⁻; Kb = [R-NH₃⁺][OH⁻]/[R-NH₂]\n• pKb = -log Kb; smaller pKb = stronger base.\n• Aliphatic amines stronger bases than ammonia (+I effect of alkyl groups).\n• Aromatic amines weaker bases than ammonia (resonance delocalisation of lone pair).\n• Order in gas phase: 3° > 2° > 1° > NH₃ (only +I effect).\n• Order in aqueous phase (methyl): (CH₃)₂NH > CH₃NH₂ > (CH₃)₃N > NH₃ (solvation effects).\n• Order in aqueous phase (ethyl): (C₂H₅)₂NH > (C₂H₅)₃N > C₂H₅NH₂ > NH₃.",
                        "hindi": "• एमीन N पर एकाकी युग्म के कारण लुईस क्षारक हैं।\n• R-NH₂ + H₂O ⇌ R-NH₃⁺ + OH⁻; Kb = [R-NH₃⁺][OH⁻]/[R-NH₂]\n• pKb = -log Kb; कम pKb = प्रबल क्षारक।\n• एलिफैटिक एमीन अमोनिया से प्रबल क्षारक (एल्किल समूहों का +I प्रभाव)।\n• एरोमैटिक एमीन अमोनिया से दुर्बल क्षारक (एकाकी युग्म का अनुनाद विस्थानीकरण)।\n• गैस प्रावस्था में क्रम: 3° > 2° > 1° > NH₃ (केवल +I प्रभाव)।\n• जलीय प्रावस्था में क्रम (मेथिल): (CH₃)₂NH > CH₃NH₂ > (CH₃)₃N > NH₃ (विलायकन प्रभाव)।\n• जलीय प्रावस्था में क्रम (एथिल): (C₂H₅)₂NH > (C₂H₅)₃N > C₂H₅NH₂ > NH₃."
                    }
                },
                {
                    "id": "concept9_4_2",
                    "display_name": {
                        "english": "Acylation and Benzoylation",
                        "hindi": "एसिलीकरण एवं बेंज़ॉयलीकरण"
                    },
                    "description": {
                        "english": "• 1° and 2° amines react with acid chlorides/anhydrides to form amides.\n• R-NH₂ + R'-COCl (pyridine) → R'-CONH-R + HCl.\n• Benzoylation: C₆H₅COCl + RNH₂ → C₆H₅CONHR (benzamide derivative).\n• 3° amines do not have replaceable H, hence no acylation.",
                        "hindi": "• 1° एवं 2° एमीन अम्ल क्लोराइड/एनहाइड्राइड के साथ अभिक्रिया करके एमाइड बनाते हैं।\n• R-NH₂ + R'-COCl (पिरिडीन) → R'-CONH-R + HCl.\n• बेंज़ॉयलीकरण: C₆H₅COCl + RNH₂ → C₆H₅CONHR (बेंजामाइड व्युत्पन्न)।\n• 3° एमीन में प्रतिस्थापन योग्य H नहीं होता, अतः एसिलीकरण नहीं होता।"
                    }
                },
                {
                    "id": "concept9_4_3",
                    "display_name": {
                        "english": "Carbylamine Reaction",
                        "hindi": "कार्बिलएमीन अभिक्रिया"
                    },
                    "description": {
                        "english": "• Test for primary amines: R-NH₂ + CHCl₃ + 3KOH (alc.) → R-NC (isocyanide, foul smell) + 3KCl + 3H₂O.\n• Secondary and tertiary amines do not give this test.",
                        "hindi": "• प्राथमिक एमीनों के लिए परीक्षण: R-NH₂ + CHCl₃ + 3KOH (एल्को.) → R-NC (आइसोसायनाइड, दुर्गंध) + 3KCl + 3H₂O.\n• द्वितीयक एवं तृतीयक एमीन यह परीक्षण नहीं देते।"
                    }
                },
                {
                    "id": "concept9_4_4",
                    "display_name": {
                        "english": "Reaction with Nitrous Acid",
                        "hindi": "नाइट्रस अम्ल के साथ अभिक्रिया"
                    },
                    "description": {
                        "english": "• 1° aliphatic amines: R-NH₂ + HNO₂ → Alcohol + N₂ (gas, used in estimation).\n• 1° aromatic amines: C₆H₅NH₂ + NaNO₂ + 2HCl (273-278K) → C₆H₅N₂⁺Cl⁻ (diazonium salt).\n• 2° amines: R₂NH + HNO₂ → R₂N-N=O (N-nitrosamine).\n• 3° aliphatic amines: React to form water-soluble salts.\n• 3° aromatic amines: Electrophilic substitution at ring.",
                        "hindi": "• 1° एलिफैटिक एमीन: R-NH₂ + HNO₂ → एल्कोहॉल + N₂ (गैस, अनुमापन में प्रयुक्त)।\n• 1° एरोमैटिक एमीन: C₆H₅NH₂ + NaNO₂ + 2HCl (273-278K) → C₆H₅N₂⁺Cl⁻ (डाइऐज़ोनियम लवण)।\n• 2° एमीन: R₂NH + HNO₂ → R₂N-N=O (N-नाइट्रोसामीन)।\n• 3° एलिफैटिक एमीन: अभिक्रिया करके जल-विलेय लवण बनाते हैं।\n• 3° एरोमैटिक एमीन: वलय पर इलेक्ट्रॉनस्नेही प्रतिस्थापन।"
                    }
                },
                {
                    "id": "concept9_4_5",
                    "display_name": {
                        "english": "Hinsberg's Test (with Arylsulphonyl Chloride)",
                        "hindi": "हिंसबर्ग परीक्षण (एरिलसल्फोनिल क्लोराइड के साथ)"
                    },
                    "description": {
                        "english": "• 1° amine: C₆H₅SO₂Cl + RNH₂ → C₆H₅SO₂NHR (sulphonamide, soluble in alkali due to acidic H).\n• 2° amine: C₆H₅SO₂Cl + R₂NH → C₆H₅SO₂NR₂ (sulphonamide, insoluble in alkali).\n• 3° amine: No reaction.",
                        "hindi": "• 1° एमीन: C₆H₅SO₂Cl + RNH₂ → C₆H₅SO₂NHR (सल्फोनामाइड, अम्लीय H के कारण क्षार में विलेय)।\n• 2° एमीन: C₆H₅SO₂Cl + R₂NH → C₆H₅SO₂NR₂ (सल्फोनामाइड, क्षार में अविलेय)।\n• 3° एमीन: कोई अभिक्रिया नहीं।"
                    }
                },
                {
                    "id": "concept9_4_6",
                    "display_name": {
                        "english": "Electrophilic Substitution of Aniline",
                        "hindi": "एनिलीन का इलेक्ट्रॉनस्नेही प्रतिस्थापन"
                    },
                    "description": {
                        "english": "• -NH₂ group is o,p-directing and strongly activating.\n• Bromination: Aniline + Br₂ water → 2,4,6-tribromoaniline (white precipitate).\n• Nitration: Direct nitration gives mixture (due to protonation in acidic medium). Protect -NH₂ by acetylation to get mainly p-nitroaniline.\n• Sulphonation: Aniline + conc. H₂SO₄ → anilinium hydrogensulphate → sulphanilic acid (p-aminobenzene sulphonic acid) on heating.\n• Aniline does not undergo Friedel-Crafts reaction (salt formation with AlCl₃).",
                        "hindi": "• -NH₂ समूह o,p-निर्देशक एवं प्रबल सक्रियकारी होता है।\n• ब्रोमीनीकरण: एनिलीन + Br₂ जल → 2,4,6-ट्राइब्रोमोएनिलीन (श्वेत अवक्षेप)।\n• नाइट्रीकरण: सीधा नाइट्रीकरण मिश्रण देता है (अम्लीय माध्यम में प्रोटॉनीकरण के कारण)। -NH₂ को एसिटिलीकरण द्वारा सुरक्षित करें ताकि मुख्यतः p-नाइट्रोएनिलीन प्राप्त हो।\n• सल्फोनीकरण: एनिलीन + सांद्र H₂SO₄ → एनिलीनियम हाइड्रोजनसल्फेट → गर्म करने पर सल्फानिलिक अम्ल (p-ऐमीनोबेन्जीन सल्फोनिक अम्ल)।\n• एनिलीन फ्रीडेल-क्राफ्ट्स अभिक्रिया नहीं करता (AlCl₃ के साथ लवण निर्माण)।"
                    }
                }
            ]
        },
        {
            "id": "topic9_5",
            "display_name": {
                "english": "DIAZONIUM SALTS",
                "hindi": "डाइऐज़ोनियम लवण"
            },
            "article_range": "Sections 9.7-9.9",
            "concepts": [
                {
                    "id": "concept9_5_1",
                    "display_name": {
                        "english": "Preparation and Properties",
                        "hindi": "विधि एवं गुण"
                    },
                    "description": {
                        "english": "• Diazotisation: C₆H₅NH₂ + NaNO₂ + 2HCl (273-278K) → C₆H₅N₂⁺Cl⁻ + NaCl + 2H₂O.\n• Arenediazonium salts are stable at low temperatures due to resonance.\n• Used immediately after preparation (decomposes in dry state or on warming).",
                        "hindi": "• डाइऐज़ोटीकरण: C₆H₅NH₂ + NaNO₂ + 2HCl (273-278K) → C₆H₅N₂⁺Cl⁻ + NaCl + 2H₂O.\n• ऐरीनडाइऐज़ोनियम लवण अनुनाद के कारण कम ताप पर स्थायी होते हैं।\n• बनाने के तुरंत बाद प्रयोग करें (शुष्क अवस्था या गर्म करने पर विघटित हो जाते हैं)।"
                    }
                },
                {
                    "id": "concept9_5_2",
                    "display_name": {
                        "english": "Reactions Involving Displacement of N₂",
                        "hindi": "N₂ के विस्थापन से संबंधित अभिक्रियाएं"
                    },
                    "description": {
                        "english": "• Sandmeyer reaction: ArN₂⁺X⁻ + CuX/HX → ArX + N₂ (X = Cl, Br, CN).\n• Gatterman reaction: ArN₂⁺Cl⁻ + Cu/HCl → ArCl + N₂.\n• Replacement by I⁻: ArN₂⁺Cl⁻ + KI → ArI + KCl + N₂.\n• Replacement by F⁻: ArN₂⁺Cl⁻ + HBF₄ → ArN₂⁺BF₄⁻ → ArF + BF₃ + N₂ (heat).\n• Replacement by H (reduction): ArN₂⁺Cl⁻ + H₃PO₂ (hypophosphorous acid) → ArH + N₂.\n• Replacement by OH: ArN₂⁺Cl⁻ + H₂O (warm) → ArOH + N₂ + HCl.\n• Replacement by NO₂: ArN₂⁺BF₄⁻ + NaNO₂/Cu → ArNO₂ + N₂.",
                        "hindi": "• सैंडमायर अभिक्रिया: ArN₂⁺X⁻ + CuX/HX → ArX + N₂ (X = Cl, Br, CN).\n• गैटरमान अभिक्रिया: ArN₂⁺Cl⁻ + Cu/HCl → ArCl + N₂.\n• I⁻ द्वारा प्रतिस्थापन: ArN₂⁺Cl⁻ + KI → ArI + KCl + N₂.\n• F⁻ द्वारा प्रतिस्थापन: ArN₂⁺Cl⁻ + HBF₄ → ArN₂⁺BF₄⁻ → ArF + BF₃ + N₂ (गर्म)।\n• H द्वारा प्रतिस्थापन (अपचयन): ArN₂⁺Cl⁻ + H₃PO₂ (हाइपोफॉस्फोरस अम्ल) → ArH + N₂.\n• OH द्वारा प्रतिस्थापन: ArN₂⁺Cl⁻ + H₂O (गर्म) → ArOH + N₂ + HCl.\n• NO₂ द्वारा प्रतिस्थापन: ArN₂⁺BF₄⁻ + NaNO₂/Cu → ArNO₂ + N₂."
                    }
                },
                {
                    "id": "concept9_5_3",
                    "display_name": {
                        "english": "Coupling Reactions",
                        "hindi": "युग्मन अभिक्रियाएं"
                    },
                    "description": {
                        "english": "• Retention of diazo group (-N=N-).\n• With phenols (in alkaline medium): ArN₂⁺Cl⁻ + C₆H₅OH → p-hydroxyazobenzene (orange dye).\n• With aromatic amines: ArN₂⁺Cl⁻ + C₆H₅NH₂ → p-aminoazobenzene (yellow dye).\n• These compounds are used as dyes (azo dyes).",
                        "hindi": "• डाइऐज़ो समूह (-N=N-) का बने रहना।\n• फिनॉल के साथ (क्षारीय माध्यम में): ArN₂⁺Cl⁻ + C₆H₅OH → p-हाइड्रॉक्सीऐज़ोबेन्जीन (नारंगी रंग)।\n• एरोमैटिक एमीन के साथ: ArN₂⁺Cl⁻ + C₆H₅NH₂ → p-ऐमीनोऐज़ोबेन्जीन (पीला रंग)।\n• ये यौगिक रंगों (ऐज़ो रंग) के रूप में प्रयुक्त होते हैं।"
                    }
                }
            ]
        }
        ]
    },

    {
    "id": "chapter10",
    "display_name": {
        "english": "CHAPTER 10: BIOMOLECULES",
        "hindi": "अध्याय 10: जैव-अणु"
    },
    "color": "#0066CC",
    "topics": [
        {
            "id": "topic10_1",
            "display_name": {
                "english": "CARBOHYDRATES",
                "hindi": "कार्बोहाइड्रेट"
            },
            "article_range": "Section 10.1",
            "concepts": [
                {
                    "id": "concept10_1_1",
                    "display_name": {
                        "english": "Classification",
                        "hindi": "वर्गीकरण"
                    },
                    "description": {
                        "english": "• Monosaccharides: Cannot be hydrolysed further (e.g., Glucose, Fructose).\n• Oligosaccharides: Yield 2-10 monosaccharide units on hydrolysis. Disaccharides: Sucrose, Maltose, Lactose.\n• Polysaccharides: Yield many monosaccharide units (e.g., Starch, Cellulose, Glycogen).\n• Reducing sugars: Reduce Fehling's/Tollens' reagent (all monosaccharides, maltose, lactose).\n• Non-reducing sugars: Sucrose.",
                        "hindi": "• मोनोसैकेराइड: आगे जल अपघटित नहीं हो सकते (जैसे, ग्लूकोस, फ्रक्टोस)।\n• ऑलिगोसैकेराइड: जल अपघटन पर 2-10 मोनोसैकेराइड इकाइयाँ देते हैं। डाइसैकेराइड: सुक्रोस, माल्टोस, लैक्टोस।\n• पॉलीसैकेराइड: अनेक मोनोसैकेराइड इकाइयाँ देते हैं (जैसे, स्टार्च, सेलुलोस, ग्लाइकोजन)।\n• अपचायक शर्करा: फेहलिंग/टॉलेन अभिकर्मक को अपचयित करती हैं (सभी मोनोसैकेराइड, माल्टोस, लैक्टोस)।\n• अनपचायक शर्करा: सुक्रोस।"
                    }
                },
                {
                    "id": "concept10_1_2",
                    "display_name": {
                        "english": "Glucose (C₆H₁₂O₆)",
                        "hindi": "ग्लूकोस (C₆H₁₂O₆)"
                    },
                    "description": {
                        "english": "• Open chain structure: Aldohexose with -CHO and five -OH groups.\n• Evidence: Forms oxime/cyanohydrin (carbonyl), gluconic acid with Br₂ water (aldehyde), glucose pentaacetate (five -OH), saccharic acid with HNO₃ (primary -OH), n-hexane with HI (straight chain).\n• Cyclic structure: Exists as α and β anomers (pyranose ring, C1 is anomeric carbon).\n• β-D-glucose is more stable and predominant in solution.",
                        "hindi": "• खुली श्रृंखला संरचना: एल्डोहेक्सोस जिसमें -CHO एवं पाँच -OH समूह हैं।\n• साक्ष्य: ऑक्सीम/सायनोहाइड्रिन बनाता है (कार्बोनिल), Br₂ जल के साथ ग्लूकोनिक अम्ल (एल्डिहाइड), ग्लूकोस पेंटाएसीटेट (पाँच -OH), HNO₃ के साथ सैकेरिक अम्ल (प्राथमिक -OH), HI के साथ n-हेक्सेन (सीधी श्रृंखला)।\n• चक्रीय संरचना: α एवं β ऐनोमर के रूप में विद्यमान (पाइरेनोस वलय, C1 ऐनोमेरिक कार्बन है)।\n• β-D-ग्लूकोस अधिक स्थायी एवं विलयन में प्रमुखता से पाया जाता है।"
                    }
                },
                {
                    "id": "concept10_1_3",
                    "display_name": {
                        "english": "Disaccharides",
                        "hindi": "डाइसैकेराइड"
                    },
                    "description": {
                        "english": "• Sucrose: Glucose + Fructose (α-1,β-2 glycosidic linkage). Non-reducing sugar. Hydrolysis gives invert sugar (dextro to laevo rotation).\n• Maltose: Glucose + Glucose (α-1→4 linkage). Reducing sugar.\n• Lactose (milk sugar): Galactose + Glucose (β-1→4 linkage). Reducing sugar.",
                        "hindi": "• सुक्रोस: ग्लूकोस + फ्रक्टोस (α-1,β-2 ग्लाइकोसिडिक बंध)। अनपचायक शर्करा। जल अपघटन पर इनवर्ट शर्करा मिलती है (डेक्स्ट्रो से लीवो घूर्णन)।\n• माल्टोस: ग्लूकोस + ग्लूकोस (α-1→4 बंध)। अपचायक शर्करा।\n• लैक्टोस (दुग्ध शर्करा): गैलेक्टोस + ग्लूकोस (β-1→4 बंध)। अपचायक शर्करा।"
                    }
                },
                {
                    "id": "concept10_1_4",
                    "display_name": {
                        "english": "Polysaccharides",
                        "hindi": "पॉलीसैकेराइड"
                    },
                    "description": {
                        "english": "• Starch: Polymer of α-glucose. Two components: Amylose (water soluble, unbranched, α-1→4 linkage) and Amylopectin (insoluble, branched, α-1→4 and α-1→6 linkage).\n• Cellulose: Polymer of β-glucose (β-1→4 linkage). Straight chain, structural component of plant cell wall. Not digested by humans.\n• Glycogen (animal starch): Highly branched polymer of α-glucose (similar to amylopectin but more branched). Storage form of glucose in animals.",
                        "hindi": "• स्टार्च: α-ग्लूकोस का बहुलक। दो घटक: एमाइलोस (जल विलेय, अशाखित, α-1→4 बंध) एवं एमाइलोपेक्टिन (अविलेय, शाखित, α-1→4 एवं α-1→6 बंध)।\n• सेलुलोस: β-ग्लूकोस का बहुलक (β-1→4 बंध)। सीधी श्रृंखला, पादप कोशिका भित्ति का संरचनात्मक घटक। मनुष्य द्वारा पाचित नहीं होता।\n• ग्लाइकोजन (प्राणि स्टार्च): α-ग्लूकोस का अत्यधिक शाखित बहुलक (एमाइलोपेक्टिन के समान किंतु अधिक शाखित)। प्राणियों में ग्लूकोस का संचित रूप।"
                    }
                }
            ]
        },
        {
            "id": "topic10_2",
            "display_name": {
                "english": "PROTEINS",
                "hindi": "प्रोटीन"
            },
            "article_range": "Section 10.2",
            "concepts": [
                {
                    "id": "concept10_2_1",
                    "display_name": {
                        "english": "Amino Acids",
                        "hindi": "एमीनो अम्ल"
                    },
                    "description": {
                        "english": "• Building blocks of proteins. Contain -NH₂ and -COOH groups.\n• α-Amino acids: Amino group attached to α-carbon (e.g., Glycine, Alanine).\n• Classification: Essential (cannot be synthesised, must be in diet, 10 types), Non-essential.\n• Based on R group: Neutral, acidic, basic.\n• Zwitter ion form: In aqueous solution, exist as dipolar ion (NH₃⁺-CHR-COO⁻). Amphoteric in nature.\n• All natural α-amino acids (except glycine) are optically active and have L-configuration.",
                        "hindi": "• प्रोटीन के निर्माण खंड। इनमें -NH₂ एवं -COOH समूह होते हैं।\n• α-एमीनो अम्ल: एमीनो समूह α-कार्बन से जुड़ा होता है (जैसे, ग्लाइसिन, ऐलेनिन)।\n• वर्गीकरण: आवश्यक (शरीर में संश्लेषित नहीं हो सकते, आहार में आवश्यक, 10 प्रकार), अनावश्यक।\n• R समूह के आधार पर: उदासीन, अम्लीय, क्षारीय।\n• ज्विटर आयन रूप: जलीय विलयन में द्विध्रुवी आयन के रूप में विद्यमान (NH₃⁺-CHR-COO⁻)। उभयधर्मी प्रकृति।\n• सभी प्राकृतिक α-एमीनो अम्ल (ग्लाइसिन को छोड़कर) प्रकाशिक सक्रिय होते हैं एवं L-विन्यास रखते हैं।"
                    }
                },
                {
                    "id": "concept10_2_2",
                    "display_name": {
                        "english": "Structure of Proteins",
                        "hindi": "प्रोटीन की संरचना"
                    },
                    "description": {
                        "english": "• Peptide bond: -CO-NH- bond formed between amino acids (amide linkage).\n• Primary structure: Sequence of amino acids in polypeptide chain.\n• Secondary structure: α-helix (intramolecular H-bonding) and β-pleated sheet (intermolecular H-bonding).\n• Tertiary structure: Overall folding of polypeptide chain (disulphide bonds, H-bonds, ionic interactions, van der Waals).\n• Quaternary structure: Arrangement of multiple polypeptide subunits (e.g., Haemoglobin).",
                        "hindi": "• पेप्टाइड बंध: एमीनो अम्लों के बीच बनने वाला -CO-NH- बंध (एमाइड बंध)।\n• प्राथमिक संरचना: पॉलीपेप्टाइड श्रृंखला में एमीनो अम्लों का अनुक्रम।\n• द्वितीयक संरचना: α-हेलिक्स (अंतराअणुक H-बंध) एवं β-प्लीटेड शीट (अंतराआण्विक H-बंध)।\n• तृतीयक संरचना: पॉलीपेप्टाइड श्रृंखला की कुल वलन संरचना (डाइसल्फाइड बंध, H-बंध, आयनिक अन्योन्य क्रियाएं, वान्डर वाल्स)।\n• चतुष्क संरचना: अनेक पॉलीपेप्टाइड उपइकाइयों की व्यवस्था (जैसे, हीमोग्लोबिन)।"
                    }
                },
                {
                    "id": "concept10_2_3",
                    "display_name": {
                        "english": "Denaturation of Proteins",
                        "hindi": "प्रोटीन का विकृतिकरण"
                    },
                    "description": {
                        "english": "• Loss of biological activity due to disruption of secondary, tertiary, quaternary structure.\n• Caused by change in pH, temperature, or by adding certain salts.\n• Primary structure remains intact.\n• Examples: Coagulation of egg white on boiling, curdling of milk.",
                        "hindi": "• द्वितीयक, तृतीयक, चतुष्क संरचना के विघटन के कारण जैविक सक्रियता का नष्ट होना।\n• pH परिवर्तन, तापमान, या कुछ लवण मिलाने के कारण होता है।\n• प्राथमिक संरचना बनी रहती है।\n• उदाहरण: उबालने पर अंडे का सफेद भाग जमना, दूध का फटना।"
                    }
                },
                {
                    "id": "concept10_2_4",
                    "display_name": {
                        "english": "Enzymes",
                        "hindi": "एंजाइम"
                    },
                    "description": {
                        "english": "• Biocatalysts, almost all are globular proteins.\n• Highly specific in action.\n• Named after substrate (e.g., maltase acts on maltose) or reaction (e.g., oxidoreductase).\n• Lower activation energy for reactions.\n• Mechanism: Lock and key model.",
                        "hindi": "• जैवउत्प्रेरक, लगभग सभी गोलाकार प्रोटीन होते हैं।\n• क्रिया में अत्यधिक विशिष्ट।\n• नामकरण क्रियाधार के नाम पर (जैसे, माल्टोस पर कार्य करने वाला माल्टेज) या अभिक्रिया के नाम पर (जैसे, ऑक्सीडोरिडक्टेज)।\n• अभिक्रियाओं के लिए सक्रियण ऊर्जा कम करते हैं।\n• क्रियाविधि: लॉक एवं की मॉडल।"
                    }
                }
            ]
        },
        {
            "id": "topic10_3",
            "display_name": {
                "english": "VITAMINS",
                "hindi": "विटामिन"
            },
            "article_range": "Section 10.4",
            "concepts": [
                {
                    "id": "concept10_3_1",
                    "display_name": {
                        "english": "Classification and Deficiency Diseases",
                        "hindi": "वर्गीकरण एवं कमी से होने वाले रोग"
                    },
                    "description": {
                        "english": "• Fat-soluble vitamins: A, D, E, K (stored in liver and adipose tissues).\n• Water-soluble vitamins: B group (B₁, B₂, B₆, B₁₂) and Vitamin C (must be supplied regularly).\n• Vitamin A: Xerophthalmia, Night blindness. Sources: Fish liver oil, carrots, milk.\n• Vitamin B₁ (Thiamine): Beri-beri. Sources: Yeast, milk, cereals.\n• Vitamin B₂ (Riboflavin): Cheilosis. Sources: Milk, egg white, liver.\n• Vitamin B₆ (Pyridoxine): Convulsions. Sources: Yeast, milk, egg yolk.\n• Vitamin B₁₂: Pernicious anaemia. Sources: Meat, fish, egg, curd.\n• Vitamin C (Ascorbic acid): Scurvy. Sources: Citrus fruits, amla, green leafy vegetables.\n• Vitamin D: Rickets (children), Osteomalacia (adults). Sources: Sunlight, fish, egg yolk.\n• Vitamin E: Increased fragility of RBCs. Sources: Vegetable oils.\n• Vitamin K: Increased blood clotting time. Sources: Green leafy vegetables.",
                        "hindi": "• वसा-विलेय विटामिन: A, D, E, K (यकृत एवं वसा ऊतकों में संचित)।\n• जल-विलेय विटामिन: B समूह (B₁, B₂, B₆, B₁₂) एवं विटामिन C (नियमित रूप से आपूर्ति आवश्यक)।\n• विटामिन A: ज़ीरॉफ़्थैल्मिया, रतौंधी। स्रोत: मछली यकृत तेल, गाजर, दूध।\n• विटामिन B₁ (थायमिन): बेरी-बेरी। स्रोत: यीस्ट, दूध, अनाज।\n• विटामिन B₂ (राइबोफ्लेविन): काइलोसिस। स्रोत: दूध, अंडे का सफेद भाग, यकृत।\n• विटामिन B₆ (पिरिडॉक्सिन): आक्षेप। स्रोत: यीस्ट, दूध, अंडे की जर्दी।\n• विटामिन B₁₂: हानिकर रक्ताल्पता। स्रोत: मांस, मछली, अंडा, दही।\n• विटामिन C (एस्कॉर्बिक अम्ल): स्कर्वी। स्रोत: खट्टे फल, आँवला, हरी पत्तेदार सब्जियाँ।\n• विटामिन D: रिकेट्स (बच्चे), ऑस्टियोमलेशिया (वयस्क)। स्रोत: सूर्य का प्रकाश, मछली, अंडे की जर्दी।\n• विटामिन E: लाल रक्त कणिकाओं की बढ़ी हुई भंगुरता। स्रोत: वनस्पति तेल।\n• विटामिन K: बढ़ा हुआ रक्त स्कंदन समय। स्रोत: हरी पत्तेदार सब्जियाँ।"
                    }
                }
            ]
        },
        {
            "id": "topic10_4",
            "display_name": {
                "english": "NUCLEIC ACIDS",
                "hindi": "न्यूक्लिक अम्ल"
            },
            "article_range": "Section 10.5",
            "concepts": [
                {
                    "id": "concept10_4_1",
                    "display_name": {
                        "english": "DNA and RNA",
                        "hindi": "DNA एवं RNA"
                    },
                    "description": {
                        "english": "• Nucleic acids are polymers of nucleotides.\n• Nucleoside = Sugar + Base. Nucleotide = Nucleoside + Phosphate.\n• DNA: Sugar = Deoxyribose; Bases = Adenine (A), Guanine (G), Cytosine (C), Thymine (T).\n• RNA: Sugar = Ribose; Bases = A, G, C, Uracil (U).\n• Primary structure: Nucleotides linked by 3'-5' phosphodiester bonds.\n• Secondary structure (DNA): Double helix (Watson-Crick model). Two strands are complementary and antiparallel. A=T (2 H-bonds), G≡C (3 H-bonds).\n• RNA: Usually single stranded. Types: mRNA, rRNA, tRNA.",
                        "hindi": "• न्यूक्लिक अम्ल, न्यूक्लियोटाइड के बहुलक हैं।\n• न्यूक्लियोसाइड = शर्करा + क्षारक। न्यूक्लियोटाइड = न्यूक्लियोसाइड + फॉस्फेट।\n• DNA: शर्करा = डीऑक्सीराइबोस; क्षारक = ऐडेनिन (A), ग्वानिन (G), साइटोसिन (C), थायमिन (T).\n• RNA: शर्करा = राइबोस; क्षारक = A, G, C, यूरेसिल (U).\n• प्राथमिक संरचना: न्यूक्लियोटाइड 3'-5' फॉस्फोडाइएस्टर बंधों द्वारा जुड़े होते हैं।\n• द्वितीयक संरचना (DNA): द्विकुंडलिनी (वाटसन-क्रिक मॉडल)। दोनों श्रृंखलाएं पूरक एवं समानांतर होती हैं। A=T (2 H-बंध), G≡C (3 H-बंध).\n• RNA: प्रायः एकल श्रृंखला। प्रकार: mRNA, rRNA, tRNA."
                    }
                },
                {
                    "id": "concept10_4_2",
                    "display_name": {
                        "english": "Biological Functions",
                        "hindi": "जैविक कार्य"
                    },
                    "description": {
                        "english": "• DNA: Chemical basis of heredity, reservoir of genetic information, self-duplicating.\n• RNA: Involved in protein synthesis (mRNA carries genetic code from DNA to ribosomes, tRNA brings amino acids, rRNA is structural component of ribosomes).\n• DNA fingerprinting: Used in forensics, paternity testing, identification.",
                        "hindi": "• DNA: आनुवंशिकता का रासायनिक आधार, आनुवंशिक सूचना का संचयकर्ता, स्व-अनुलिपिकारक।\n• RNA: प्रोटीन संश्लेषण में शामिल (mRNA DNA से आनुवंशिक कोड राइबोसोम तक ले जाता है, tRNA एमीनो अम्ल लाता है, rRNA राइबोसोम का संरचनात्मक घटक है)।\n• DNA फिंगरप्रिंटिंग: फोरेंसिक, पितृत्व परीक्षण, पहचान में प्रयुक्त।"
                    }
                }
            ]
        }
        ]
    }
    # add here 
  


        
    ]
}

# ============================================
# LAYOUT CONFIGURATION
# ============================================
LAYOUT_CONFIG = {
    "column_x": {
        "chemistry": 150,
        "chapter": 550,
        "topic": 1100,
        "concept": 1600,
        "description": 2000
    },
    "spacing": {
        "parent_child_gap": 100,
        "block_gap": 50,
        "description_offset": 80
    },
    "box_sizes": {
        "base_width": 200,
        "base_height": 70,
        "topic_width": 280,
        "description_width": 1000,
        "chars_per_line": {
            "english": 35,
            "hindi": 35
        },
        "line_height": 18,
        "text_sizing": {
            "char_width": {
                "english": 7.5,
                "hindi": 9.0
            },
            "padding": 40,
            "min_width": 200,
            "max_width": 450,
            "multi_line_threshold": 40
        }
    },
    "colors": {
        "chemistry": "#FF9933",
        "chapter": "#4ecdc4",
        "topic": "#FFB6C1",
        "concept": "#ffe8a3",
        "description": "#c7e9c0"
    }
}

# ============================================
# STREAMLIT UI
# ============================================

st.sidebar.title("Language Settings / भाषा सेटिंग्स")
selected_language = st.sidebar.radio(
    "Select Language / भाषा चुनें",
    options=list(LANGUAGES.keys()),
    format_func=lambda x: LANGUAGES[x],
    key="chemistry_language_selector"  # ← यह line add करें
)

st.sidebar.markdown("---")
st.sidebar.title("Instructions / निर्देश")
if selected_language == "english":
    st.sidebar.markdown("""
    - **Click** on CHEMISTRY to show/hide everything
    - **Double-click** on any CHAPTER to expand/collapse
    - **Double-click** on any TOPIC to expand/collapse
    - **Double-click** on any CONCEPT to show/hide details
    - **Double-click** on details to hide them
    """)
else:
    st.sidebar.markdown("""
    - **क्लिक करें** रसायन विज्ञान पर सब कुछ दिखाने/छिपाने के लिए
    - **डबल-क्लिक करें** किसी भी अध्याय पर विस्तार/संक्षिप्त करने के लिए
    - **डबल-क्लिक करें** किसी भी विषय पर विस्तार/संक्षिप्त करने के लिए
    - **डबल-क्लिक करें** किसी भी अवधारणा पर विवरण दिखाने/छिपाने के लिए
    - **डबल-क्लिक करें** विवरण पर उसे छिपाने के लिए
    """)

st.title("Chemistry Mind Map / रसायन विज्ञान माइंड मैप")
st.caption(f"Subject: Chemistry | विषय: रसायन विज्ञान")

# ============================================
# GENERATE HTML
# ============================================

def generate_bilingual_html(config, layout, language):
    """Generate HTML/JS"""
    
    import json
    
    # Create language-specific config
    lang_config = {
        "title": config["title"][language],
        "chapters": []
    }
    
    for chapter in config["chapters"]:
        lang_chapter = {
            "id": chapter["id"],
            "display_name": chapter["display_name"][language],
            "color": chapter["color"],
            "topics": []
        }
        
        for topic in chapter["topics"]:
            lang_topic = {
                "id": topic["id"],
                "display_name": topic["display_name"][language],
                "article_range": topic["article_range"],
                "hasTopic": True,
                "concepts": []
            }
            
            for concept in topic["concepts"]:
                lang_topic["concepts"].append({
                    "id": concept["id"],
                    "display_name": concept["display_name"][language],
                    "description": concept["description"][language],
                    "hasTopic": True
                })
            
            lang_chapter["topics"].append(lang_topic)
        
        lang_config["chapters"].append(lang_chapter)
    
    chapters_json = json.dumps(lang_config["chapters"])
    layout_json = json.dumps(layout)
    chemistry_title = lang_config["title"]
    
    html = f"""
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<style>
body {{
    margin: 0;
    overflow: auto;
    background: #eef2f7;
    font-family: {('Arial' if language == 'english' else 'Arial, "Noto Sans Devanagari", "Nirmala UI", sans-serif')};
}}
#container {{
    width: 2500px;
    min-height: 1000px;
    position: relative;
}}
canvas {{
    display: block;
    border: 1px solid #ccc;
}}
.language-badge {{
    position: fixed;
    top: 10px;
    right: 10px;
    background: rgba(255,255,255,0.9);
    padding: 5px 10px;
    border-radius: 5px;
    font-size: 12px;
    z-index: 1000;
}}
</style>
</head>
<body>
<div class="language-badge">{LANGUAGES[language]}</div>
<div id="container">
    <canvas id="canvas"></canvas>
</div>

<script>
// Configuration
const chaptersConfig = {chapters_json};
const layoutConfig = {layout_json};
const CHEMISTRY_TITLE = "{chemistry_title}";
const CURRENT_LANGUAGE = "{language}";

document.addEventListener('DOMContentLoaded', function() {{
    const canvas = document.getElementById("canvas");
    if (!canvas) {{
        console.error("Canvas not found!");
        return;
    }}
    
    const ctx = canvas.getContext("2d");
    if (!ctx) {{
        console.error("Context not found!");
        return;
    }}

    // Build lookup dictionaries
    let conceptDisplayNames = {{}};
    let conceptDescriptions = {{}};
    let conceptHasTopic = {{}};
    let allConcepts = [];
    let topicConcepts = {{}};
    let chapterTopics = {{}};
    
    chaptersConfig.forEach(chapter => {{
        if (chapter.topics) {{
            chapterTopics[chapter.id] = chapter.topics.map(t => t.id);
            
            chapter.topics.forEach(topic => {{
                topicConcepts[topic.id] = topic.concepts.map(c => c.id);
                
                topic.concepts.forEach(concept => {{
                    conceptDisplayNames[concept.id] = concept.display_name;
                    conceptDescriptions[concept.id] = concept.description;
                    conceptHasTopic[concept.id] = true;
                    allConcepts.push(concept.id);
                }});
            }});
        }}
    }});

    // State management
    let states = {{
        chemistry: true
    }};
    
    chaptersConfig.forEach(chapter => {{
        states[chapter.id] = false;
        
        if (chapter.topics) {{
            chapter.topics.forEach(topic => {{
                states[topic.id] = false;
            }});
        }}
    }});
    
    let conceptStates = {{}};
    allConcepts.forEach(concept => {{
        conceptStates[concept] = false;
    }});
    
    let nodes = {{}};

    // Layout constants
    const COLUMN_X = layoutConfig.column_x;
    const PARENT_CHILD_GAP = layoutConfig.spacing.parent_child_gap;
    const BLOCK_GAP = layoutConfig.spacing.block_gap;
    
    const BASE_WIDTH = layoutConfig.box_sizes.base_width;
    const BASE_HEIGHT = layoutConfig.box_sizes.base_height;
    const TOPIC_WIDTH = layoutConfig.box_sizes.topic_width;
    
    const COLOR_CHEMISTRY = layoutConfig.colors.chemistry;
    const COLOR_CHAPTER = layoutConfig.colors.chapter;
    const COLOR_TOPIC = layoutConfig.colors.topic;
    const COLOR_CONCEPT = layoutConfig.colors.concept;
    const COLOR_DESCRIPTION = layoutConfig.colors.description;

    // Helper function to check collision
    function checkCollision(newNode, existingNodes, excludeId) {{
        for (let id in existingNodes) {{
            if (id === excludeId) continue;
            
            let other = existingNodes[id];
            if (!other) continue;
            
            let xOverlap = Math.abs(newNode.x - other.x) < (newNode.width/2 + other.width/2 + 40);
            let yOverlap = Math.abs(newNode.y - other.y) < (newNode.height/2 + other.height/2 + 30);
            
            if (xOverlap && yOverlap) {{
                return true;
            }}
        }}
        return false;
    }}

    // Calculate box size based on text
    function calculateBoxSize(text, type) {{
        let width = BASE_WIDTH;
        let height = BASE_HEIGHT;
        
        const ctx = document.createElement('canvas').getContext('2d');
        
        if (CURRENT_LANGUAGE === 'hindi') {{
            ctx.font = (type === "description") ? "11px 'Nirmala UI', 'Noto Sans Devanagari', Arial" : "bold 12px 'Nirmala UI', 'Noto Sans Devanagari', Arial";
        }} else {{
            ctx.font = (type === "description") ? "11px Arial" : "bold 12px Arial";
        }}
        
        const padding = 20;
        const lineHeight = 18;
        const maxWidth = type === "description" ? 500 : 450;
        
        let words = text.split(' ');
        let lines = [];
        let currentLine = '';
        
        for (let i = 0; i < words.length; i++) {{
            let testLine = currentLine + (currentLine ? ' ' : '') + words[i];
            let metrics = ctx.measureText(testLine);
            
            if (metrics.width < maxWidth - padding) {{
                currentLine = testLine;
            }} else {{
                if (currentLine) {{
                    lines.push(currentLine);
                }}
                currentLine = words[i];
            }}
        }}
        if (currentLine) {{
            lines.push(currentLine);
        }}
        
        let maxLineWidth = 0;
        for (let j = 0; j < lines.length; j++) {{
            let metrics = ctx.measureText(lines[j]);
            if (metrics.width > maxLineWidth) {{
                maxLineWidth = metrics.width;
            }}
        }}
        
        width = Math.min(maxWidth, maxLineWidth + padding * 2);
        height = Math.max(BASE_HEIGHT, lines.length * lineHeight + padding);
        
        return {{ width: width, height: height }};
    }}

    // Draw curved connection
    function drawCurvedConnection(startNode, endNode) {{
        if(!startNode || !endNode) return;
        
        let startX = startNode.x;
        let startY = startNode.y - startNode.height/2;
        
        let endX = endNode.x - endNode.width/2 + 10;
        let endY = endNode.y;
        
        const distance = Math.abs(endX - startX);
        const verticalDistance = Math.abs(endY - startY);
        
        let cp1x, cp1y, cp2x, cp2y;
        
        cp1x = startX + distance * 0.3;
        cp1y = startY + verticalDistance * 0.2;
        cp2x = endX - distance * 0.2;
        cp2y = endY - verticalDistance * 0.1;
        
        ctx.beginPath();
        ctx.moveTo(startX, startY);
        ctx.bezierCurveTo(cp1x, cp1y, cp2x, cp2y, endX, endY);
        
        ctx.strokeStyle = "#666";
        ctx.lineWidth = 2;
        ctx.setLineDash([]);
        
        ctx.stroke();
    }}

    // Draw node with text
    function drawNode(n) {{
        if (!n) return;
        
        let x = n.x - n.width/2;
        let y = n.y - n.height/2;
        let width = n.width;
        let height = n.height;
        
        // Draw expansion indicator for collapsed nodes with children
        if (hasChildren(n) && !isExpanded(n)) {{
            let colors = ["#FF9933", "#AAAAAA", "#138808"];
            let offset = 4;
            
            for (let i = 0; i < 3; i++) {{
                let backX = x - (i * 2);
                let backY = y + (i * offset);
                let backWidth = width + (i * 4);
                let backHeight = height;
                
                let visiblePortion = 20;
                let clipY = backY + backHeight - visiblePortion;
                
                ctx.save();
                
                ctx.beginPath();
                ctx.rect(x - 10, clipY, width + 20, visiblePortion + 10);
                ctx.clip();
                
                let radius = Math.min(10, backHeight * 0.15);
                ctx.beginPath();
                ctx.moveTo(backX + radius, backY);
                ctx.lineTo(backX + backWidth - radius, backY);
                ctx.quadraticCurveTo(backX + backWidth, backY, backX + backWidth, backY + radius);
                ctx.lineTo(backX + backWidth, backY + backHeight - radius);
                ctx.quadraticCurveTo(backX + backWidth, backY + backHeight, backX + backWidth - radius, backY + backHeight);
                ctx.lineTo(backX + radius, backY + backHeight);
                ctx.quadraticCurveTo(backX, backY + backHeight, backX, backY + backHeight - radius);
                ctx.lineTo(backX, backY + radius);
                ctx.quadraticCurveTo(backX, backY, backX + radius, backY);
                ctx.closePath();
                
                ctx.fillStyle = colors[i] + "30";
                ctx.fill();
                ctx.strokeStyle = colors[i];
                ctx.lineWidth = 1;
                ctx.stroke();
                
                ctx.restore();
            }}
        }}
        
        // Draw main rectangle
        let radius = Math.min(15, height * 0.2);
        
        ctx.beginPath();
        ctx.moveTo(x + radius, y);
        ctx.lineTo(x + width - radius, y);
        ctx.quadraticCurveTo(x + width, y, x + width, y + radius);
        ctx.lineTo(x + width, y + height - radius);
        ctx.quadraticCurveTo(x + width, y + height, x + width - radius, y + height);
        ctx.lineTo(x + radius, y + height);
        ctx.quadraticCurveTo(x, y + height, x, y + height - radius);
        ctx.lineTo(x, y + radius);
        ctx.quadraticCurveTo(x, y, x + radius, y);
        ctx.closePath();
        
        ctx.fillStyle = n.color;
        ctx.fill();
        ctx.strokeStyle = "#333";
        ctx.lineWidth = 2;
        ctx.stroke();
        
        // Draw text with wrapping
        ctx.fillStyle = "#000";
        if (CURRENT_LANGUAGE === 'hindi') {{
            ctx.font = (n.type === "description") ? "11px 'Nirmala UI', 'Noto Sans Devanagari', Arial" : "bold 12px 'Nirmala UI', 'Noto Sans Devanagari', Arial";
        }} else {{
            ctx.font = (n.type === "description") ? "11px Arial" : "bold 12px Arial";
        }}
        ctx.textAlign = "center";
        ctx.textBaseline = "middle";
        
        let words = n.text.split(' ');
        let lines = [];
        let currentLine = '';
        const maxWidth = n.type === "description" ? 480 : (n.type === "chemistry" ? 600 : 400);
        
        for (let i = 0; i < words.length; i++) {{
            let testLine = currentLine + (currentLine ? ' ' : '') + words[i];
            let metrics = ctx.measureText(testLine);
            
            if (metrics.width < maxWidth) {{
                currentLine = testLine;
            }} else {{
                if (currentLine) {{
                    lines.push(currentLine);
                }}
                currentLine = words[i];
            }}
        }}
        if (currentLine) {{
            lines.push(currentLine);
        }}
        
        const lineHeight = 18;
        let startY = y + height/2 - ((lines.length - 1) * lineHeight)/2;
        lines.forEach((line, index) => {{
            ctx.fillText(line, x + width/2, startY + index * lineHeight);
        }});
    }}

    function hasChildren(node) {{
        if (node.type === "chemistry") {{
            return true;
        }}
        else if (node.type === "chapter") {{
            let chapter = chaptersConfig.find(c => c.id === node.chapterId);
            return chapter && chapter.topics && chapter.topics.length > 0;
        }}
        else if (node.type === "topic") {{
            for (let chapter of chaptersConfig) {{
                if (chapter.topics) {{
                    let topic = chapter.topics.find(t => t.id === node.topicId);
                    if (topic && topic.concepts && topic.concepts.length > 0) {{
                        return true;
                    }}
                }}
            }}
            return false;
        }}
        else if (node.type === "concept") {{
            return true;
        }}
        return false;
    }}

    function isExpanded(node) {{
        if (node.type === "chemistry") {{
            return states.chemistry;
        }}
        else if (node.type === "chapter") {{
            return states[node.chapterId];
        }}
        else if (node.type === "topic") {{
            return states[node.topicId];
        }}
        else if (node.type === "concept") {{
            return conceptStates[node.conceptId];
        }}
        return false;
    }}

    // Calculate layout
    function calculateLayout() {{
        nodes = {{}};
        
        if(states.chemistry === true)  {{
            let yCursor = 150;
            
            chaptersConfig.forEach(chapter => {{
                let childrenHeight = 0;

                if(states[chapter.id]) {{
                    if (chapter.topics) {{
                        childrenHeight = chapter.topics.reduce((total, topic) => {{
                            total += PARENT_CHILD_GAP;
                            
                            if(states[topic.id]) {{
                                let topicChildrenHeight = topic.concepts.reduce((topicTotal, c) => {{
                                    topicTotal += PARENT_CHILD_GAP;
                                    if(conceptStates[c.id]) {{
                                        let descSize = calculateBoxSize(conceptDescriptions[c.id], "description");
                                        topicTotal += descSize.height + 40;
                                    }}
                                    return topicTotal;
                                }}, 0);
                                
                                let topicSize = calculateBoxSize(topic.display_name + " [" + topic.article_range + "]", "topic");
                                total += Math.max(topicSize.height, topicChildrenHeight);
                            }} else {{
                                let topicSize = calculateBoxSize(topic.display_name + " [" + topic.article_range + "]", "topic");
                                total += topicSize.height;
                            }}
                            
                            return total;
                        }}, 0);
                    }}
                }}

                let chapterSize = calculateBoxSize(chapter.display_name, "chapter");
                let blockHeight = Math.max(chapterSize.height, childrenHeight);
                let parentY = yCursor + blockHeight/2;

                nodes[chapter.id] = {{
                    x: COLUMN_X.chapter,
                    y: parentY,
                    width: chapterSize.width,
                    height: chapterSize.height,
                    text: chapter.display_name,
                    color: chapter.color || COLOR_CHAPTER,
                    type: "chapter",
                    chapterId: chapter.id
                }};

                if(states[chapter.id]) {{
                    let startY = parentY - childrenHeight/2 + PARENT_CHILD_GAP/2;
                    let currentY = startY;

                    if (chapter.topics) {{
                        chapter.topics.forEach(topic => {{
                            let topicChildrenHeight = 0;
                            
                            if(states[topic.id]) {{
                                topicChildrenHeight = topic.concepts.reduce((total, c) => {{
                                    total += PARENT_CHILD_GAP;
                                    if(conceptStates[c.id]) {{
                                        let descSize = calculateBoxSize(conceptDescriptions[c.id], "description");
                                        total += descSize.height + 40;
                                    }}
                                    return total;
                                }}, 0);
                            }}
                            
                            let topicDisplayName = topic.display_name + " [" + topic.article_range + "]";
                            let topicSize = calculateBoxSize(topicDisplayName, "topic");
                            let topicBlockHeight = Math.max(topicSize.height, topicChildrenHeight);
                            let topicY = currentY + topicBlockHeight/2;
                            
                            nodes[topic.id] = {{
                                x: COLUMN_X.topic,
                                y: topicY,
                                width: topicSize.width,
                                height: topicSize.height,
                                text: topicDisplayName,
                                color: COLOR_TOPIC,
                                type: "topic",
                                topicId: topic.id,
                                chapterId: chapter.id
                            }};
                            
                            if(states[topic.id]) {{
                                let topicStartY = topicY - topicChildrenHeight/2 + PARENT_CHILD_GAP/2;
                                let topicCurrentY = topicStartY;
                                
                                topic.concepts.forEach(c => {{
                                    let conceptSize = calculateBoxSize(conceptDisplayNames[c.id], "concept");
                                    
                                    nodes[c.id] = {{
                                        x: COLUMN_X.concept,
                                        y: topicCurrentY,
                                        width: conceptSize.width,
                                        height: conceptSize.height,
                                        text: conceptDisplayNames[c.id],
                                        color: COLOR_CONCEPT,
                                        type: "concept",
                                        conceptId: c.id,
                                        topicId: topic.id,
                                        chapterId: chapter.id
                                    }};
                                    
                                    topicCurrentY += PARENT_CHILD_GAP;
                                    
                                    if(conceptStates[c.id]) {{
                                        let descId = c.id + "_desc";
                                        let descSize = calculateBoxSize(conceptDescriptions[c.id], "description");
                                        
                                        let descY = nodes[c.id].y + nodes[c.id].height/2 + descSize.height/2 + 50;
                                        let descX = COLUMN_X.description;
                                        
                                        let tempNode = {{
                                            x: descX,
                                            y: descY,
                                            width: descSize.width,
                                            height: descSize.height
                                        }};
                                        
                                        let attempts = 0;
                                        while (checkCollision(tempNode, nodes, descId) && attempts < 15) {{
                                            descY += descSize.height + 30;
                                            tempNode.y = descY;
                                            attempts++;
                                        }}
                                        
                                        nodes[descId] = {{
                                            x: descX,
                                            y: descY,
                                            width: descSize.width,
                                            height: descSize.height,
                                            text: conceptDescriptions[c.id],
                                            color: COLOR_DESCRIPTION,
                                            type: "description",
                                            parentId: c.id,
                                            conceptId: c.id
                                        }};
                                        
                                        topicCurrentY += descSize.height + 50;
                                    }}
                                }});
                            }}
                            
                            currentY += topicBlockHeight + PARENT_CHILD_GAP;
                        }});
                    }}
                }}

                yCursor += blockHeight + BLOCK_GAP;
            }});
            
            canvas.height = yCursor + 150;
        }} else {{
            canvas.height = 300;
        }}
        
        let chemSize = calculateBoxSize(CHEMISTRY_TITLE, "chemistry");
        let chemY = states.chemistry ? canvas.height/2 : 150;
        
        nodes.chemistry = {{
            x: COLUMN_X.chemistry,
            y: chemY,
            width: chemSize.width,
            height: chemSize.height,
            text: CHEMISTRY_TITLE,
            color: COLOR_CHEMISTRY,
            type: "chemistry"
        }};

        canvas.width = 2500;
    }}

    // Draw everything
    function draw() {{
        ctx.clearRect(0, 0, canvas.width, canvas.height);
        ctx.beginPath();
       
        calculateLayout();

        if(states.chemistry === true) {{
            // Draw connections
            chaptersConfig.forEach(chapter => {{
                if(nodes[chapter.id]) drawCurvedConnection(nodes.chemistry, nodes[chapter.id]);
            }});

            chaptersConfig.forEach(chapter => {{
                if(states[chapter.id] && nodes[chapter.id]) {{
                    if (chapter.topics) {{
                        chapter.topics.forEach(topic => {{
                            if(nodes[topic.id]) drawCurvedConnection(nodes[chapter.id], nodes[topic.id]);
                            
                            if(states[topic.id]) {{
                                topic.concepts.forEach(c => {{
                                    if(nodes[c.id]) {{
                                        drawCurvedConnection(nodes[topic.id], nodes[c.id]);
                                        
                                        if(conceptStates[c.id] && nodes[c.id + "_desc"]) {{
                                            drawCurvedConnection(nodes[c.id], nodes[c.id + "_desc"]);
                                        }}
                                    }}
                                }});
                            }}
                        }});
                    }}
                }}
            }});
        }}

        Object.values(nodes).forEach(drawNode);
    }}

    // Interaction handlers
    function inside(mx, my, n) {{
        if(!n) return false;
        return mx >= n.x - n.width/2 && 
               mx <= n.x + n.width/2 && 
               my >= n.y - n.height/2 && 
               my <= n.y + n.height/2;
    }}

    canvas.addEventListener("click", e => {{
        const rect = canvas.getBoundingClientRect();
        const scaleX = canvas.width / rect.width;
        const scaleY = canvas.height / rect.height;
        
        const mx = (e.clientX - rect.left) * scaleX;
        const my = (e.clientY - rect.top) * scaleY;
        
        if(nodes.chemistry && inside(mx, my, nodes.chemistry)) {{
            states.chemistry = !states.chemistry;
            
            if(!states.chemistry) {{
                chaptersConfig.forEach(chapter => {{
                    states[chapter.id] = false;
                    if (chapter.topics) {{
                        chapter.topics.forEach(topic => {{
                            states[topic.id] = false;
                            topic.concepts.forEach(c => conceptStates[c.id] = false);
                        }});
                    }}
                }});
            }}
            draw();
            return;
        }}
        
        if(!states.chemistry) return;
    }});

    canvas.addEventListener("dblclick", e => {{
        const rect = canvas.getBoundingClientRect();
        const scaleX = canvas.width / rect.width;
        const scaleY = canvas.height / rect.height;
        
        const mx = (e.clientX - rect.left) * scaleX;
        const my = (e.clientY - rect.top) * scaleY;
        
        let found = false;
        
        if(!states.chemistry) return;
        
        // Check chapters
        for(let chapter of chaptersConfig) {{
            if(!found && nodes[chapter.id] && inside(mx, my, nodes[chapter.id])) {{
                states[chapter.id] = !states[chapter.id];
                if(!states[chapter.id]) {{
                    if (chapter.topics) {{
                        chapter.topics.forEach(topic => {{
                            states[topic.id] = false;
                            topic.concepts.forEach(c => conceptStates[c.id] = false);
                        }});
                    }}
                }}
                draw();
                found = true;
                break;
            }}
        }}
        
        // Check topics
        if(!found) {{
            for(let chapter of chaptersConfig) {{
                if(chapter.topics) {{
                    for(let topic of chapter.topics) {{
                        if(!found && nodes[topic.id] && inside(mx, my, nodes[topic.id])) {{
                            states[topic.id] = !states[topic.id];
                            if(!states[topic.id]) {{
                                topic.concepts.forEach(c => conceptStates[c.id] = false);
                            }}
                            draw();
                            found = true;
                            break;
                        }}
                    }}
                }}
                if(found) break;
            }}
        }}
        
        // Check concepts
        if(!found) {{
            for(let conceptId of allConcepts) {{
                if(!found && nodes[conceptId] && inside(mx, my, nodes[conceptId])) {{
                    conceptStates[conceptId] = !conceptStates[conceptId];
                    draw();
                    found = true;
                    break;
                }}
            }}
        }}
        
        // Check descriptions
        if(!found) {{
            for(let conceptId of allConcepts) {{
                let descId = conceptId + "_desc";
                if(!found && nodes[descId] && inside(mx, my, nodes[descId])) {{
                    conceptStates[conceptId] = false;
                    draw();
                    found = true;
                    break;
                }}
            }}
        }}
    }});

    draw();
    console.log(`Canvas initialized with ${{CURRENT_LANGUAGE}} language`);
}});
</script>
</body>
</html>
"""
    return html

# Generate and display
html_content = generate_bilingual_html(CHEMISTRY_CONFIG, LAYOUT_CONFIG, selected_language)
components.html(html_content, height=900, scrolling=True)

# ============================================
# FOOTER
# ============================================
st.markdown("---")
col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("### 📚 About")
    if selected_language == "english":
        st.markdown("""
        **Chemistry Mind Map** - Complete Chapter 1 & 2
        
        **Chapter 1:** Chemical Reactions and Equations
        - Chemical Reactions (8 concepts)
        - Effects of Oxidation (2 concepts)
        
        **Chapter 2:** Acids, Bases and Salts
        - Chemical Properties of Acids & Bases (7 concepts)
        - Acids, Bases and Their Strength (6 concepts)
        - Salts and Their Compounds (8 concepts)
        
        Complete with examples and equations
        """)
    else:
        st.markdown("""
        **रसायन विज्ञान माइंड मैप** - संपूर्ण अध्याय 1 एवं 2
        
        **अध्याय 1:** रासायनिक अभिक्रियाएं और समीकरण
        - रासायनिक अभिक्रियाएं (8 अवधारणाएं)
        - ऑक्सीकरण के प्रभाव (2 अवधारणाएं)
        
        **अध्याय 2:** अम्ल, क्षारक एवं लवण
        - अम्लों एवं क्षारकों के रासायनिक गुणधर्म (7 अवधारणाएं)
        - अम्ल, क्षारक एवं उनकी प्रबलता (6 अवधारणाएं)
        - लवण एवं उनके यौगिक (8 अवधारणाएं)
        
        उदाहरण और समीकरणों के साथ
        """)

with col2:
    st.markdown("### 🎯 How to Use")
    if selected_language == "english":
        st.markdown("""
        1. **Click** CHEMISTRY to show/hide all
        2. **Double-click** any CHAPTER to expand
        3. **Double-click** any TOPIC to expand
        4. **Double-click** any CONCEPT for details
        5. **Double-click** details to hide
        """)
    else:
        st.markdown("""
        1. **क्लिक करें** रसायन विज्ञान पर सब दिखाने/छिपाने के लिए
        2. **डबल-क्लिक करें** किसी भी अध्याय पर विस्तार करने के लिए
        3. **डबल-क्लिक करें** किसी भी विषय पर विस्तार करने के लिए
        4. **डबल-क्लिक करें** किसी भी अवधारणा पर विवरण के लिए
        5. **डबल-क्लिक करें** विवरण पर छिपाने के लिए
        """)

with col3:
    st.markdown("### 📊 Content")
    if selected_language == "english":
        total_chapters = len(CHEMISTRY_CONFIG["chapters"])
        total_topics = 0
        total_concepts = 0
        for chapter in CHEMISTRY_CONFIG["chapters"]:
            total_topics += len(chapter["topics"])
            for topic in chapter["topics"]:
                total_concepts += len(topic["concepts"])
        
        st.markdown(f"""
        **Chemistry Content:**
        - Chapters: {total_chapters}
        - Topics: {total_topics}
        - Concepts: {total_concepts}
        - Chemical equations: 30+
        - Bilingual: English/Hindi
        """)
    else:
        total_chapters = len(CHEMISTRY_CONFIG["chapters"])
        total_topics = 0
        total_concepts = 0
        for chapter in CHEMISTRY_CONFIG["chapters"]:
            total_topics += len(chapter["topics"])
            for topic in chapter["topics"]:
                total_concepts += len(topic["concepts"])
        
        st.markdown(f"""
        **रसायन विज्ञान सामग्री:**
        - अध्याय: {total_chapters}
        - विषय: {total_topics}
        - अवधारणाएं: {total_concepts}
        - रासायनिक समीकरण: 30+
        - द्विभाषी: अंग्रेजी/हिंदी
        """)

# Debug
if st.checkbox("Show Debug Info / डीबग जानकारी दिखाएं"):
    total_chapters = len(CHEMISTRY_CONFIG["chapters"])
    total_topics = 0
    total_concepts = 0
    for chapter in CHEMISTRY_CONFIG["chapters"]:
        total_topics += len(chapter["topics"])
        for topic in chapter["topics"]:
            total_concepts += len(topic["concepts"])
    
    st.json({
        "main_title": "CHEMISTRY",
        "total_chapters": total_chapters,
        "total_topics": total_topics,
        "total_concepts": total_concepts,
        "current_language": selected_language
    })
