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
# PHYSICS CONFIGURATION - EMPTY STRUCTURE
# ============================================
# NOTE: Paste your PHYSICS_CONFIG content here
PHYSICS_CONFIG = {
    "title": {
        "english": "PHYSICS12",
        "hindi": "भौतिक विज्ञान"
    },
    "chapters": [
        # ============================================
        # CHAPTER 1: ELECTRIC CHARGES AND FIELDS
        # ============================================
        {
            "id": "chapter1",
            "display_name": {
                "english": "CHAPTER 1: ELECTRIC CHARGES AND FIELDS",
                "hindi": "अध्याय 1: वैद्युत आवेश तथा क्षेत्र"
            },
            "color": "#FF9933",
            "topics": [
                {
                    "id": "topic1_1",
                    "display_name": {
                        "english": "ELECTRIC CHARGE",
                        "hindi": "वैद्युत आवेश"
                    },
                    "article_range": "Sections 1.2-1.4",
                    "concepts": [
                        {
                            "id": "concept1_1_1",
                            "display_name": {
                                "english": "Basic Properties of Charge",
                                "hindi": "आवेश के मूल गुण"
                            },
                            "description": {
                                "english": "• Additivity: Total charge is algebraic sum.\n• Conservation: Total charge of an isolated system is constant.\n• Quantisation: q = ne, where n is an integer and e = 1.6 x 10⁻¹⁹ C.",
                                "hindi": "• योगात्मकता: कुल आवेश बीजगणितीय योग होता है।\n• संरक्षण: किसी विलगित निकाय का कुल आवेश स्थिर रहता है।\n• क्वांटीकरण: q = ne, जहाँ n एक पूर्णांक है तथा e = 1.6 x 10⁻¹⁹ C."
                            }
                        },
                        {
                            "id": "concept1_1_2",
                            "display_name": {
                                "english": "Charging by Induction",
                                "hindi": "प्रेरण द्वारा आवेशन"
                            },
                            "description": {
                                "english": "Process of charging a conductor without physical contact. A charged object induces opposite charge on one end and same charge on the other end of a conductor.",
                                "hindi": "बिना भौतिक संपर्क के चालक को आवेशित करने की प्रक्रिया। कोई आवेशित वस्तु चालक के एक सिरे पर विपरीत तथा दूसरे सिरे पर समान आवेश प्रेरित करती है।"
                            }
                        }
                    ]
                },
                {
                    "id": "topic1_2",
                    "display_name": {
                        "english": "COULOMB'S LAW & FORCES",
                        "hindi": "कूलॉम का नियम एवं बल"
                    },
                    "article_range": "Sections 1.5-1.6",
                    "concepts": [
                        {
                            "id": "concept1_2_1",
                            "display_name": {
                                "english": "Coulomb's Law",
                                "hindi": "कूलॉम का नियम"
                            },
                            "description": {
                                "english": "Force between two point charges: F = (1/4πε₀) * |q₁q₂|/r² \n\n1/4πε₀ = 9 x 10⁹ Nm²/C².\nIt acts along the line joining the two charges.",
                                "hindi": "दो बिंदु आवेशों के बीच बल: F = (1/4πε₀) * |q₁q₂|/r² \n\n1/4πε₀ = 9 x 10⁹ Nm²/C².\nयह दोनों आवेशों को मिलाने वाली रेखा के अनुदिश कार्य करता है।"
                            }
                        },
                        {
                            "id": "concept1_2_2",
                            "display_name": {
                                "english": "Forces Between Multiple Charges",
                                "hindi": "अनेक आवेशों के बीच बल"
                            },
                            "description": {
                                "english": "Principle of Superposition: Net force on a charge is the vector sum of forces from all other individual charges.\nF₁ = F₁₂ + F₁₃ + ... + F₁ₙ",
                                "hindi": "अध्यारोपण का सिद्धांत: किसी आवेश पर नेट बल अन्य सभी व्यष्टिगत आवेशों के कारण लगने वाले बलों का सदिश योग होता है।\nF₁ = F₁₂ + F₁₃ + ... + F₁ₙ"
                            }
                        }
                    ]
                },
                {
                    "id": "topic1_3",
                    "display_name": {
                        "english": "ELECTRIC FIELD",
                        "hindi": "वैद्युत क्षेत्र"
                    },
                    "article_range": "Section 1.7",
                    "concepts": [
                        {
                            "id": "concept1_3_1",
                            "display_name": {
                                "english": "Electric Field (E)",
                                "hindi": "वैद्युत क्षेत्र (E)"
                            },
                            "description": {
                                "english": "Force experienced by a unit positive charge. E = F/q₀ (test charge).\nDue to point charge Q: E = (1/4πε₀) * Q/r²  (radially outward for +Q, inward for -Q).",
                                "hindi": "एकांत धन आवेश द्वारा अनुभव किया गया बल। E = F/q₀ (परीक्षण आवेश)।\nबिंदु आवेश Q के कारण: E = (1/4πε₀) * Q/r² (+Q के लिए त्रिज्यतः बाहर, -Q के लिए अंदर)।"
                            }
                        },
                        {
                            "id": "concept1_3_2",
                            "display_name": {
                                "english": "Electric Field Lines",
                                "hindi": "वैद्युत क्षेत्र रेखाएँ"
                            },
                            "description": {
                                "english": "• Start at +ve charges, end at -ve charges.\n• Tangent gives direction of E.\n• Density gives magnitude of E.\n• Never intersect.",
                                "hindi": "• धन आवेश से शुरू, ऋण आवेश पर समाप्त।\n• स्पर्श रेखा E की दिशा बताती है।\n• घनत्व E का परिमाण बताता है।\n• कभी नहीं काटतीं।"
                            }
                        }
                    ]
                },
                {
                    "id": "topic1_4",
                    "display_name": {
                        "english": "ELECTRIC FLUX & GAUSS'S LAW",
                        "hindi": "वैद्युत फ्लक्स एवं गॉस का नियम"
                    },
                    "article_range": "Sections 1.9-1.14",
                    "concepts": [
                        {
                            "id": "concept1_4_1",
                            "display_name": {
                                "english": "Electric Flux (Φ)",
                                "hindi": "वैद्युत फ्लक्स (Φ)"
                            },
                            "description": {
                                "english": "Measure of electric field through a surface. ΔΦ = E·ΔS = E ΔS cosθ.\nFor a closed surface, Φ = ∮E·dS.",
                                "hindi": "किसी सतह से गुजरने वाले वैद्युत क्षेत्र का माप। ΔΦ = E·ΔS = E ΔS cosθ.\nबंद सतह के लिए, Φ = ∮E·dS."
                            }
                        },
                        {
                            "id": "concept1_4_2",
                            "display_name": {
                                "english": "Gauss's Law",
                                "hindi": "गॉस का नियम"
                            },
                            "description": {
                                "english": "Total flux through a closed surface is (1/ε₀) times the charge enclosed (q_enclosed).\n∮E·dS = q_enclosed / ε₀",
                                "hindi": "किसी बंद सतह से कुल फ्लक्स, सतह द्वारा परिबद्ध आवेश (q_enclosed) का (1/ε₀) गुना होता है।\n∮E·dS = q_enclosed / ε₀"
                            }
                        },
                        {
                            "id": "concept1_4_3",
                            "display_name": {
                                "english": "Applications of Gauss's Law",
                                "hindi": "गॉस के नियम के अनुप्रयोग"
                            },
                            "description": {
                                "english": "• Inf. line charge (λ): E = λ/(2πε₀r) (radial)\n• Inf. plane sheet (σ): E = σ/(2ε₀) (⊥ to sheet)\n• Spherical shell (q):\n  - Outside (r>R): E = (1/4πε₀)q/r²\n  - Inside (r<R): E = 0",
                                "hindi": "• अनंत रेखीय आवेश (λ): E = λ/(2πε₀r) (त्रिज्य)\n• अनंत समतल चादर (σ): E = σ/(2ε₀) (चादर के लंबवत)\n• गोलीय कोश (q):\n  - बाहर (r>R): E = (1/4πε₀)q/r²\n  - अंदर (r<R): E = 0"
                            }
                        }
                    ]
                }
            ]
        },
        # ============================================
        # CHAPTER 2: ELECTROSTATIC POTENTIAL AND CAPACITANCE
        # ============================================
        {
            "id": "chapter2",
            "display_name": {
                "english": "CHAPTER 2: ELECTROSTATIC POTENTIAL AND CAPACITANCE",
                "hindi": "अध्याय 2: स्थिरवैद्युत विभव एवं धारिता"
            },
            "color": "#0066CC",
            "topics": [
                {
                    "id": "topic2_1",
                    "display_name": {
                        "english": "ELECTROSTATIC POTENTIAL",
                        "hindi": "स्थिरवैद्युत विभव"
                    },
                    "article_range": "Sections 2.2-2.5",
                    "concepts": [
                        {
                            "id": "concept2_1_1",
                            "display_name": {
                                "english": "Electric Potential (V)",
                                "hindi": "वैद्युत विभव (V)"
                            },
                            "description": {
                                "english": "Work done per unit charge in bringing a test charge from infinity to that point.\nV = W/q₀ (Potential at infinity is 0).\nDue to point charge Q: V = (1/4πε₀) * Q/r",
                                "hindi": "परीक्षण आवेश को अनंत से उस बिंदु तक लाने में प्रति इकाई आवेश पर किया गया कार्य।\nV = W/q₀ (अनंत पर विभव 0 होता है)।\nबिंदु आवेश Q के कारण: V = (1/4πε₀) * Q/r"
                            }
                        },
                        {
                            "id": "concept2_1_2",
                            "display_name": {
                                "english": "Potential due to an Electric Dipole",
                                "hindi": "वैद्युत द्विध्रुव के कारण विभव"
                            },
                            "description": {
                                "english": "At a point far away (r>>a): V = (1/4πε₀) * (p cosθ)/r² \nwhere p = q(2a) is the dipole moment.",
                                "hindi": "दूरस्थ बिंदु पर (r>>a): V = (1/4πε₀) * (p cosθ)/r² \nजहाँ p = q(2a) द्विध्रुव आघूर्ण है।"
                            }
                        },
                        {
                            "id": "concept2_1_3",
                            "display_name": {
                                "english": "Equipotential Surfaces",
                                "hindi": "समविभव पृष्ठ"
                            },
                            "description": {
                                "english": "Surface with constant potential.\n• E is perpendicular to the surface.\n• No work is done moving a charge on it.\n• For point charge: concentric spheres.",
                                "hindi": "स्थिर विभव वाला पृष्ठ।\n• E सतह के लंबवत होता है।\n• इस पर आवेश को विस्थापित करने में कोई कार्य नहीं होता।\n• बिंदु आवेश के लिए: संकेंद्रित गोले।"
                            }
                        }
                    ]
                },
                {
                    "id": "topic2_2",
                    "display_name": {
                        "english": "POTENTIAL ENERGY",
                        "hindi": "स्थितिज ऊर्जा"
                    },
                    "article_range": "Sections 2.7-2.8",
                    "concepts": [
                        {
                            "id": "concept2_2_1",
                            "display_name": {
                                "english": "Potential Energy of Charge System",
                                "hindi": "आवेश निकाय की स्थितिज ऊर्जा"
                            },
                            "description": {
                                "english": "Work done to assemble the charges.\nFor two charges q₁ and q₂: U = (1/4πε₀) * (q₁q₂)/r₁₂",
                                "hindi": "आवेशों को उनके स्थानों पर रखने में किया गया कार्य।\nदो आवेशों q₁ व q₂ के लिए: U = (1/4πε₀) * (q₁q₂)/r₁₂"
                            }
                        },
                        {
                            "id": "concept2_2_2",
                            "display_name": {
                                "english": "Potential Energy in External Field",
                                "hindi": "बाह्य क्षेत्र में स्थितिज ऊर्जा"
                            },
                            "description": {
                                "english": "• For a single charge q: U = qV(r)\n• For a dipole: U = -p·E = -pE cosθ\n  (Stable equil. at θ=0°, Unstable at θ=180°)",
                                "hindi": "• एकल आवेश q के लिए: U = qV(r)\n• द्विध्रुव के लिए: U = -p·E = -pE cosθ\n  (स्थायी साम्य θ=0° पर, अस्थायी θ=180° पर)"
                            }
                        }
                    ]
                },
                {
                    "id": "topic2_3",
                    "display_name": {
                        "english": "CAPACITORS",
                        "hindi": "संधारित्र"
                    },
                    "article_range": "Sections 2.11-2.15",
                    "concepts": [
                        {
                            "id": "concept2_3_1",
                            "display_name": {
                                "english": "Capacitance (C)",
                                "hindi": "धारिता (C)"
                            },
                            "description": {
                                "english": "Ability to store charge. C = Q/V\nUnit: Farad (F).\nDepends on geometry and dielectric medium.",
                                "hindi": "आवेश संग्रह करने की क्षमता। C = Q/V\nमात्रक: फैरड (F)।\nज्यामिति एवं परावैद्युत माध्यम पर निर्भर करती है।"
                            }
                        },
                        {
                            "id": "concept2_3_2",
                            "display_name": {
                                "english": "Parallel Plate Capacitor",
                                "hindi": "समांतर प्लेट संधारित्र"
                            },
                            "description": {
                                "english": "Capacitance: C = ε₀A/d (Vacuum)\nWith dielectric: C = Kε₀A/d = εA/d\nwhere K is dielectric constant.",
                                "hindi": "धारिता: C = ε₀A/d (निर्वात में)\nपरावैद्युत सहित: C = Kε₀A/d = εA/d\nजहाँ K परावैद्युतांक है।"
                            }
                        },
                        {
                            "id": "concept2_3_3",
                            "display_name": {
                                "english": "Combination of Capacitors",
                                "hindi": "संधारित्रों का संयोजन"
                            },
                            "description": {
                                "english": "• Series: 1/C_eq = 1/C₁ + 1/C₂ + ... (V divides, Q same)\n• Parallel: C_eq = C₁ + C₂ + ... (V same, Q divides)",
                                "hindi": "• श्रेणीक्रम: 1/C_tुल्य = 1/C₁ + 1/C₂ + ... (V का विभाजन, Q समान)\n• समांतरक्रम: C_tुल्य = C₁ + C₂ + ... (V समान, Q का विभाजन)"
                            }
                        },
                        {
                            "id": "concept2_3_4",
                            "display_name": {
                                "english": "Energy Stored in a Capacitor",
                                "hindi": "संधारित्र में संचित ऊर्जा"
                            },
                            "description": {
                                "english": "U = (1/2)CV² = (1/2)QV = Q²/(2C)\nEnergy density (electric field): u = (1/2)ε₀E²",
                                "hindi": "U = (1/2)CV² = (1/2)QV = Q²/(2C)\nऊर्जा घनत्व (वैद्युत क्षेत्र): u = (1/2)ε₀E²"
                            }
                        }
                    ]
                }
            ]
        },
        # ============================================
        # CHAPTER 3: CURRENT ELECTRICITY
        # ============================================
        {
            "id": "chapter3",
            "display_name": {
                "english": "CHAPTER 3: CURRENT ELECTRICITY",
                "hindi": "अध्याय 3: विद्युत धारा"
            },
            "color": "#138808",
            "topics": [
                {
                    "id": "topic3_1",
                    "display_name": {
                        "english": "ELECTRIC CURRENT AND RESISTANCE",
                        "hindi": "विद्युत धारा एवं प्रतिरोध"
                    },
                    "article_range": "Sections 3.2-3.7",
                    "concepts": [
                        {
                            "id": "concept3_1_1",
                            "display_name": {
                                "english": "Electric Current",
                                "hindi": "विद्युत धारा"
                            },
                            "description": {
                                "english": "Rate of flow of charge: I = dQ/dt\nUnit: Ampere (A).\nDirection: flow of positive charge.",
                                "hindi": "आवेश के प्रवाह की दर: I = dQ/dt\nमात्रक: एम्पियर (A)।\nदिशा: धन आवेश के प्रवाह की दिशा।"
                            }
                        },
                        {
                            "id": "concept3_1_2",
                            "display_name": {
                                "english": "Ohm's Law",
                                "hindi": "ओम का नियम"
                            },
                            "description": {
                                "english": "At constant temp., V ∝ I.  V = IR\nwhere R is the resistance. Unit: Ohm (Ω).",
                                "hindi": "स्थिर ताप पर, V ∝ I.  V = IR\nजहाँ R प्रतिरोध है। मात्रक: ओम (Ω)।"
                            }
                        },
                        {
                            "id": "concept3_1_3",
                            "display_name": {
                                "english": "Resistivity & Conductivity",
                                "hindi": "प्रतिरोधकता एवं चालकता"
                            },
                            "description": {
                                "english": "R = ρ (l/A), where ρ is resistivity.\nσ = 1/ρ is conductivity.\nρ depends on material and temperature.",
                                "hindi": "R = ρ (l/A), जहाँ ρ प्रतिरोधकता है।\nσ = 1/ρ चालकता है।\nρ पदार्थ एवं तापमान पर निर्भर करता है।"
                            }
                        }
                    ]
                },
                {
                    "id": "topic3_2",
                    "display_name": {
                        "english": "DRIFT OF ELECTRONS",
                        "hindi": "इलेक्ट्रॉनों का अपवाह"
                    },
                    "article_range": "Section 3.5",
                    "concepts": [
                        {
                            "id": "concept3_2_1",
                            "display_name": {
                                "english": "Drift Velocity (vd)",
                                "hindi": "अपवाह वेग (vd)"
                            },
                            "description": {
                                "english": "Average velocity of electrons due to E-field. vd = (eE/m)τ\nCurrent: I = neA vd\nMobility: μ = |vd| / E",
                                "hindi": "E-क्षेत्र के कारण इलेक्ट्रॉनों का औसत वेग। vd = (eE/m)τ\nधारा: I = neA vd\nगतिशीलता: μ = |vd| / E"
                            }
                        }
                    ]
                },
                {
                    "id": "topic3_3",
                    "display_name": {
                        "english": "CIRCUITS & KIRCHHOFF'S LAWS",
                        "hindi": "परिपथ एवं किरचॉफ के नियम"
                    },
                    "article_range": "Sections 3.10-3.12",
                    "concepts": [
                        {
                            "id": "concept3_3_1",
                            "display_name": {
                                "english": "EMF and Internal Resistance",
                                "hindi": "वि. वा. बल एवं आंतरिक प्रतिरोध"
                            },
                            "description": {
                                "english": "EMF (ε): Potential difference across cell terminals when no current flows.\nInternal resistance (r): Resistance offered by electrolyte.\nTerminal voltage: V = ε - Ir",
                                "hindi": "वि. वा. बल (ε): जब कोई धारा न बहे तो सेल के सिरों का विभवांतर।\nआंतरिक प्रतिरोध (r): इलेक्ट्रोलाइट द्वारा प्रदत्त प्रतिरोध।\nटर्मिनल वोल्टता: V = ε - Ir"
                            }
                        },
                        {
                            "id": "concept3_3_2",
                            "display_name": {
                                "english": "Kirchhoff's Rules",
                                "hindi": "किरचॉफ के नियम"
                            },
                            "description": {
                                "english": "1. Junction Rule: ΣI_in = ΣI_out (Charge conservation)\n2. Loop Rule: ΣΔV = 0 around any closed loop (Energy conservation).",
                                "hindi": "1. संधि नियम: ΣI_अंदर = ΣI_बाहर (आवेश संरक्षण)\n2. लूप नियम: किसी बंद लूप में ΣΔV = 0 (ऊर्जा संरक्षण)।"
                            }
                        }
                    ]
                },
                {
                    "id": "topic3_4",
                    "display_name": {
                        "english": "HEATING EFFECT & POWER",
                        "hindi": "तापीय प्रभाव एवं शक्ति"
                    },
                    "article_range": "Section 3.9",
                    "concepts": [
                        {
                            "id": "concept3_4_1",
                            "display_name": {
                                "english": "Electrical Power & Energy",
                                "hindi": "विद्युत शक्ति एवं ऊर्जा"
                            },
                            "description": {
                                "english": "Power: P = VI = I²R = V²/R\nEnergy (Heat): H = I²Rt (Joule's Law of Heating)\nCommercial unit: 1 kWh = 3.6 x 10⁶ J",
                                "hindi": "शक्ति: P = VI = I²R = V²/R\nऊर्जा (ऊष्मा): H = I²Rt (जूल का तापन नियम)\nवाणिज्यिक मात्रक: 1 kWh = 3.6 x 10⁶ J"
                            }
                        }
                    ]
                }
            ]
        },
        # ============================================
        # CHAPTER 4: MOVING CHARGES AND MAGNETISM
        # ============================================
        {
            "id": "chapter4",
            "display_name": {
                "english": "CHAPTER 4: MOVING CHARGES AND MAGNETISM",
                "hindi": "अध्याय 4: गतिमान आवेश और चुंबकत्व"
            },
            "color": "#FFD700",
            "topics": [
                {
                    "id": "topic4_1",
                    "display_name": {
                        "english": "MAGNETIC FORCE",
                        "hindi": "चुंबकीय बल"
                    },
                    "article_range": "Section 4.2",
                    "concepts": [
                        {
                            "id": "concept4_1_1",
                            "display_name": {
                                "english": "Lorentz Force",
                                "hindi": "लॉरेंज बल"
                            },
                            "description": {
                                "english": "Force on charge q moving with velocity v in E and B fields: F = q(E + v×B)\nMagnetic force: F = q(v×B) ⇒ |F| = qvB sinθ\nDirection: ⊥ to both v and B (Right-hand rule).",
                                "hindi": "E एवं B क्षेत्रों में v वेग से गतिमान आवेश q पर बल: F = q(E + v×B)\nचुंबकीय बल: F = q(v×B) ⇒ |F| = qvB sinθ\nदिशा: v एवं B दोनों के लंबवत (दाएँ हाथ का नियम)।"
                            }
                        },
                        {
                            "id": "concept4_1_2",
                            "display_name": {
                                "english": "Force on Current-Carrying Conductor",
                                "hindi": "धारावाही चालक पर बल"
                            },
                            "description": {
                                "english": "F = I (l × B)\nwhere l is length vector in direction of current I.",
                                "hindi": "F = I (l × B)\nजहाँ l धारा I की दिशा में लंबाई सदिश है।"
                            }
                        }
                    ]
                },
                {
                    "id": "topic4_2",
                    "display_name": {
                        "english": "MOTION IN MAGNETIC FIELD",
                        "hindi": "चुंबकीय क्षेत्र में गति"
                    },
                    "article_range": "Section 4.3",
                    "concepts": [
                        {
                            "id": "concept4_2_1",
                            "display_name": {
                                "english": "Radius and Frequency",
                                "hindi": "त्रिज्या एवं आवृत्ति"
                            },
                            "description": {
                                "english": "If v ⟂ B, motion is circular.\nRadius: r = mv/qB\nAngular Frequency (Cyclotron): ω = qB/m \nFrequency: ν = qB/2πm (independent of v & r).",
                                "hindi": "यदि v ⟂ B, गति वृत्ताकार है।\nत्रिज्या: r = mv/qB\nकोणीय आवृत्ति (साइक्लोट्रॉन): ω = qB/m \nआवृत्ति: ν = qB/2πm (v एवं r से स्वतंत्र)।"
                            }
                        }
                    ]
                },
                {
                    "id": "topic4_3",
                    "display_name": {
                        "english": "MAGNETIC FIELD DUE TO CURRENT",
                        "hindi": "धारा के कारण चुंबकीय क्षेत्र"
                    },
                    "article_range": "Sections 4.4-4.7",
                    "concepts": [
                        {
                            "id": "concept4_3_1",
                            "display_name": {
                                "english": "Biot-Savart Law",
                                "hindi": "बायो-सेवार्ट नियम"
                            },
                            "description": {
                                "english": "Field due to current element Idl: dB = (μ₀/4π) (I dl × r̂)/r²\nMagnitude: dB = (μ₀/4π) (I dl sinθ)/r²\nμ₀/4π = 10⁻⁷ Tm/A",
                                "hindi": "धारा अवयव Idl के कारण क्षेत्र: dB = (μ₀/4π) (I dl × r̂)/r²\nपरिमाण: dB = (μ₀/4π) (I dl sinθ)/r²\nμ₀/4π = 10⁻⁷ Tm/A"
                            }
                        },
                        {
                            "id": "concept4_3_2",
                            "display_name": {
                                "english": "Applications of Biot-Savart Law",
                                "hindi": "बायो-सेवार्ट नियम के अनुप्रयोग"
                            },
                            "description": {
                                "english": "• Straight wire: B = μ₀I/(2πr)\n• Circular coil (centre): B = μ₀I/(2R)\n• Circular coil (axis, x>>R): B ≈ μ₀IR²/(2x³)",
                                "hindi": "• सीधे तार के लिए: B = μ₀I/(2πr)\n• वृत्ताकार कुंडली (केंद्र पर): B = μ₀I/(2R)\n• वृत्ताकार कुंडली (अक्ष पर, x>>R): B ≈ μ₀IR²/(2x³)"
                            }
                        },
                        {
                            "id": "concept4_3_3",
                            "display_name": {
                                "english": "Ampere's Circuital Law",
                                "hindi": "एम्पियर का परिपथीय नियम"
                            },
                            "description": {
                                "english": "∮ B·dl = μ₀ I_enclosed\nUsed for symmetrical current distributions.\nApplication: Solenoid (B = μ₀nI), Toroid.",
                                "hindi": "∮ B·dl = μ₀ I_परिबद्ध\nसममित धारा वितरणों के लिए प्रयुक्त।\nअनुप्रयोग: परिनालिका (B = μ₀nI), टोरॉयड।"
                            }
                        }
                    ]
                },
                {
                    "id": "topic4_4",
                    "display_name": {
                        "english": "FORCE BETWEEN CURRENTS",
                        "hindi": "धाराओं के बीच बल"
                    },
                    "article_range": "Section 4.8",
                    "concepts": [
                        {
                            "id": "concept4_4_1",
                            "display_name": {
                                "english": "Force Between Parallel Wires",
                                "hindi": "समांतर तारों के बीच बल"
                            },
                            "description": {
                                "english": "Force per unit length: f = (μ₀ I₁ I₂)/(2πd)\nSame direction currents → attract.\nOpposite direction currents → repel.\nUsed to define Ampere.",
                                "hindi": "प्रति इकाई लंबाई बल: f = (μ₀ I₁ I₂)/(2πd)\nसमान दिशा की धाराएँ → आकर्षण।\nविपरीत दिशा की धाराएँ → प्रतिकर्षण।\nएम्पियर की परिभाषा में प्रयुक्त।"
                            }
                        }
                    ]
                },
                {
                    "id": "topic4_5",
                    "display_name": {
                        "english": "TORQUE ON A LOOP",
                        "hindi": "लूप पर बल आघूर्ण"
                    },
                    "article_range": "Section 4.9",
                    "concepts": [
                        {
                            "id": "concept4_5_1",
                            "display_name": {
                                "english": "Magnetic Moment & Torque",
                                "hindi": "चुंबकीय आघूर्ण एवं बल आघूर्ण"
                            },
                            "description": {
                                "english": "Magnetic moment: m = N I A\nTorque on loop in uniform B: τ = m × B (|τ| = mB sinθ)\nMoving Coil Galvanometer works on this principle.",
                                "hindi": "चुंबकीय आघूर्ण: m = N I A\nएकसमान B में लूप पर बल आघूर्ण: τ = m × B (|τ| = mB sinθ)\nचल कुंडली गैल्वेनोमीटर इसी सिद्धांत पर कार्य करता है।"
                            }
                        }
                    ]
                }
            ]
        },
        # ============================================
        # CHAPTER 5: MAGNETISM AND MATTER
        # ============================================
        {
            "id": "chapter5",
            "display_name": {
                "english": "CHAPTER 5: MAGNETISM AND MATTER",
                "hindi": "अध्याय 5: चुंबकत्व एवं द्रव्य"
            },
            "color": "#FF9933",
            "topics": [
                {
                    "id": "topic5_1",
                    "display_name": {
                        "english": "MAGNETS AND DIPOLES",
                        "hindi": "चुंबक एवं द्विध्रुव"
                    },
                    "article_range": "Section 5.2",
                    "concepts": [
                        {
                            "id": "concept5_1_1",
                            "display_name": {
                                "english": "Bar Magnet as a Solenoid",
                                "hindi": "छड़ चुंबक एक परिनालिका के रूप में"
                            },
                            "description": {
                                "english": "A bar magnet produces the same field as a solenoid. Its magnetic moment is m = NIA for the equivalent solenoid.",
                                "hindi": "छड़ चुंबक, परिनालिका के समान क्षेत्र उत्पन्न करता है। इसका चुंबकीय आघूर्ण, तुल्य परिनालिका के लिए m = NIA होता है।"
                            }
                        },
                        {
                            "id": "concept5_1_2",
                            "display_name": {
                                "english": "Dipole in a Uniform Field",
                                "hindi": "एकसमान क्षेत्र में द्विध्रुव"
                            },
                            "description": {
                                "english": "• Torque: τ = m × B\n• Potential Energy: U = -m·B = -mB cosθ\nStable equilibrium at θ=0°, unstable at θ=180°.",
                                "hindi": "• बल आघूर्ण: τ = m × B\n• स्थितिज ऊर्जा: U = -m·B = -mB cosθ\nस्थायी साम्य θ=0° पर, अस्थायी θ=180° पर।"
                            }
                        },
                        {
                            "id": "concept5_1_3",
                            "display_name": {
                                "english": "Gauss's Law for Magnetism",
                                "hindi": "चुंबकत्व के लिए गॉस का नियम"
                            },
                            "description": {
                                "english": "The net magnetic flux through any closed surface is zero.\n∮ B·dS = 0\nThis implies magnetic monopoles do not exist.",
                                "hindi": "किसी भी बंद सतह से गुजरने वाला नेट चुंबकीय फ्लक्स शून्य होता है।\n∮ B·dS = 0\nइसका तात्पर्य है कि चुंबकीय एकध्रुव नहीं होते।"
                            }
                        }
                    ]
                },
                {
                    "id": "topic5_2",
                    "display_name": {
                        "english": "MAGNETIC PROPERTIES OF MATERIALS",
                        "hindi": "पदार्थों के चुंबकीय गुण"
                    },
                    "article_range": "Sections 5.4-5.5",
                    "concepts": [
                        {
                            "id": "concept5_2_1",
                            "display_name": {
                                "english": "Magnetisation & Magnetic Intensity",
                                "hindi": "चुंबकन एवं चुंबकीय तीव्रता"
                            },
                            "description": {
                                "english": "• Magnetisation M: Net magnetic moment per unit volume.\n• Magnetic Intensity H: B₀/μ₀ (external).\n• Relation: B = μ₀(H + M) = μH, where μ is permeability.\n• Magnetic susceptibility: χ = M/H. μ = μ₀(1+χ).",
                                "hindi": "• चुंबकन M: प्रति इकाई आयतन नेट चुंबकीय आघूर्ण।\n• चुंबकीय तीव्रता H: B₀/μ₀ (बाह्य)।\n• संबंध: B = μ₀(H + M) = μH, जहाँ μ पारगम्यता है।\n• चुंबकीय प्रवृत्ति: χ = M/H. μ = μ₀(1+χ)।"
                            }
                        },
                        {
                            "id": "concept5_2_2",
                            "display_name": {
                                "english": "Types of Magnetic Materials",
                                "hindi": "चुंबकीय पदार्थों के प्रकार"
                            },
                            "description": {
                                "english": "• Diamagnetic: χ < 0, μ_r < 1, weak repulsion (e.g., Bi, Cu).\n• Paramagnetic: χ > 0 (small), μ_r > 1, weak attraction (e.g., Al, Na).\n• Ferromagnetic: χ >> 1, μ_r >> 1, strong attraction, shows hysteresis and domains (e.g., Fe, Ni).",
                                "hindi": "• प्रतिचुंबकीय: χ < 0, μ_r < 1, दुर्बल प्रतिकर्षण (जैसे, Bi, Cu).\n• अनुचुंबकीय: χ > 0 (अल्प), μ_r > 1, दुर्बल आकर्षण (जैसे, Al, Na).\n• लौहचुंबकीय: χ >> 1, μ_r >> 1, प्रबल आकर्षण, शैथिल्य एवं डोमेन दर्शाता है (जैसे, Fe, Ni)."
                            }
                        }
                    ]
                }
            ]
        },
        # ============================================
        # CHAPTER 6: ELECTROMAGNETIC INDUCTION
        # ============================================
        {
            "id": "chapter6",
            "display_name": {
                "english": "CHAPTER 6: ELECTROMAGNETIC INDUCTION",
                "hindi": "अध्याय 6: वैद्युतचुंबकीय प्रेरण"
            },
            "color": "#0066CC",
            "topics": [
                {
                    "id": "topic6_1",
                    "display_name": {
                        "english": "FARADAY'S LAW",
                        "hindi": "फैराडे का नियम"
                    },
                    "article_range": "Sections 6.2-6.4",
                    "concepts": [
                        {
                            "id": "concept6_1_1",
                            "display_name": {
                                "english": "Magnetic Flux",
                                "hindi": "चुंबकीय फ्लक्स"
                            },
                            "description": {
                                "english": "Φ_B = B·A = BA cosθ\nUnit: Weber (Wb) or T m².\nIt is a scalar quantity.",
                                "hindi": "Φ_B = B·A = BA cosθ\nमात्रक: वेबर (Wb) या T m²।\nयह एक अदिश राशि है।"
                            }
                        },
                        {
                            "id": "concept6_1_2",
                            "display_name": {
                                "english": "Faraday's Law of Induction",
                                "hindi": "फैराडे का प्रेरण का नियम"
                            },
                            "description": {
                                "english": "The magnitude of induced emf is the rate of change of magnetic flux.\nε = -N (dΦ_B/dt) (for N turns).\nThe negative sign indicates the direction (Lenz's Law).",
                                "hindi": "प्रेरित वि. वा. बल का परिमाण चुंबकीय फ्लक्स के परिवर्तन की दर के बराबर होता है।\nε = -N (dΦ_B/dt) (N फेरों के लिए)।\nऋणात्मक चिन्ह दिशा को दर्शाता है (लेंज का नियम)।"
                            }
                        }
                    ]
                },
                {
                    "id": "topic6_2",
                    "display_name": {
                        "english": "LENZ'S LAW & MOTIONAL EMF",
                        "hindi": "लेंज का नियम एवं गति संबंधी वि. वा. बल"
                    },
                    "article_range": "Sections 6.5-6.6",
                    "concepts": [
                        {
                            "id": "concept6_2_1",
                            "display_name": {
                                "english": "Lenz's Law",
                                "hindi": "लेंज का नियम"
                            },
                            "description": {
                                "english": "The induced current opposes the change in magnetic flux that produced it.\nIt is a consequence of energy conservation.",
                                "hindi": "प्रेरित धारा, उस चुंबकीय फ्लक्स के परिवर्तन का विरोध करती है जिसके कारण वह उत्पन्न होती है।\nयह ऊर्जा संरक्षण का परिणाम है।"
                            }
                        },
                        {
                            "id": "concept6_2_2",
                            "display_name": {
                                "english": "Motional EMF",
                                "hindi": "गति संबंधी वि. वा. बल"
                            },
                            "description": {
                                "english": "EMF induced in a rod of length l moving with velocity v ⟂ to B.\nε = Blv\nDerived from Lorentz force on free electrons.",
                                "hindi": "B के लंबवत v वेग से गतिमान l लंबाई की छड़ में प्रेरित वि. वा. बल।\nε = Blv\nमुक्त इलेक्ट्रॉनों पर लॉरेंज बल से व्युत्पन्न।"
                            }
                        }
                    ]
                },
                {
                    "id": "topic6_3",
                    "display_name": {
                        "english": "INDUCTANCE",
                        "hindi": "प्रेरकत्व"
                    },
                    "article_range": "Section 6.7",
                    "concepts": [
                        {
                            "id": "concept6_3_1",
                            "display_name": {
                                "english": "Mutual Inductance (M)",
                                "hindi": "अन्योन्य प्रेरकत्व (M)"
                            },
                            "description": {
                                "english": "Flux linked with coil 2 due to current in coil 1: N₂Φ₂ = M I₁.\nInduced emf in coil 2: ε₂ = -M (dI₁/dt).\nM depends on geometry and separation of coils.",
                                "hindi": "कुंडली 1 में धारा के कारण कुंडली 2 से संबद्ध फ्लक्स: N₂Φ₂ = M I₁.\nकुंडली 2 में प्रेरित वि. वा. बल: ε₂ = -M (dI₁/dt).\nM, कुंडलियों की ज्यामिति एवं दूरी पर निर्भर करता है।"
                            }
                        },
                        {
                            "id": "concept6_3_2",
                            "display_name": {
                                "english": "Self-Inductance (L)",
                                "hindi": "स्व-प्रेरकत्व (L)"
                            },
                            "description": {
                                "english": "Flux linked with a coil due to its own current: NΦ = L I.\nBack emf: ε = -L (dI/dt).\nFor a solenoid: L = μ₀ n² A l.\nEnergy stored in inductor: U = (1/2) L I².",
                                "hindi": "स्वयं की धारा के कारण कुंडली से संबद्ध फ्लक्स: NΦ = L I.\nपश्च वि. वा. बल: ε = -L (dI/dt).\nपरिनालिका के लिए: L = μ₀ n² A l.\nप्रेरक में संचित ऊर्जा: U = (1/2) L I²."
                            }
                        }
                    ]
                },
                {
                    "id": "topic6_4",
                    "display_name": {
                        "english": "AC GENERATOR",
                        "hindi": "प्रत्यावर्ती धारा जनित्र"
                    },
                    "article_range": "Section 6.8",
                    "concepts": [
                        {
                            "id": "concept6_4_1",
                            "display_name": {
                                "english": "AC Generator Principle",
                                "hindi": "प्रत्यावर्ती धारा जनित्र का सिद्धांत"
                            },
                            "description": {
                                "english": "Converts mechanical energy to electrical energy. Based on Faraday's Law.\nA coil rotating in a magnetic field produces sinusoidal emf.\nε = NBAω sin(ωt) = ε₀ sin(ωt)",
                                "hindi": "यांत्रिक ऊर्जा को विद्युत ऊर्जा में बदलता है। फैराडे के नियम पर आधारित।\nचुंबकीय क्षेत्र में घूमती कुंडली ज्यावक्रीय वि. वा. बल उत्पन्न करती है।\nε = NBAω sin(ωt) = ε₀ sin(ωt)"
                            }
                        }
                    ]
                }
            ]
        },
        # ============================================
        # CHAPTER 7: ALTERNATING CURRENT
        # ============================================
        {
            "id": "chapter7",
            "display_name": {
                "english": "CHAPTER 7: ALTERNATING CURRENT",
                "hindi": "अध्याय 7: प्रत्यावर्ती धारा"
            },
            "color": "#138808",
            "topics": [
                {
                    "id": "topic7_1",
                    "display_name": {
                        "english": "AC VOLTAGE AND CURRENT",
                        "hindi": "प्रत्यावर्ती वोल्टता एवं धारा"
                    },
                    "article_range": "Sections 7.2-7.3",
                    "concepts": [
                        {
                            "id": "concept7_1_1",
                            "display_name": {
                                "english": "AC & RMS Values",
                                "hindi": "प्रत्यावर्ती धारा एवं वर्ग माध्य मूल मान"
                            },
                            "description": {
                                "english": "AC Voltage: v = v_m sin ωt\nRMS Current: I = i_m/√2\nRMS Voltage: V = v_m/√2\nRMS values are used for power calculations.",
                                "hindi": "प्रत्यावर्ती वोल्टता: v = v_m sin ωt\nवर्ग माध्य मूल धारा: I = i_m/√2\nवर्ग माध्य मूल वोल्टता: V = v_m/√2\nशक्ति की गणना हेतु वर्ग माध्य मूल मान प्रयुक्त होते हैं।"
                            }
                        },
                        {
                            "id": "concept7_1_2",
                            "display_name": {
                                "english": "AC through a Resistor",
                                "hindi": "प्रतिरोधक में प्रत्यावर्ती धारा"
                            },
                            "description": {
                                "english": "Current and voltage are in phase (φ=0).\ni = i_m sin ωt, where i_m = v_m/R.\nPower: P = I²R = V I",
                                "hindi": "धारा एवं वोल्टता समान कला में होते हैं (φ=0).\ni = i_m sin ωt, जहाँ i_m = v_m/R.\nशक्ति: P = I²R = V I"
                            }
                        }
                    ]
                },
                {
                    "id": "topic7_2",
                    "display_name": {
                        "english": "AC THROUGH L AND C",
                        "hindi": "L एवं C में प्रत्यावर्ती धारा"
                    },
                    "article_range": "Sections 7.4-7.5",
                    "concepts": [
                        {
                            "id": "concept7_2_1",
                            "display_name": {
                                "english": "AC through an Inductor",
                                "hindi": "प्रेरक में प्रत्यावर्ती धारा"
                            },
                            "description": {
                                "english": "Current lags voltage by π/2.\ni = i_m sin(ωt - π/2), i_m = v_m / X_L\nInductive Reactance: X_L = ωL (depends on freq.)\nAverage Power = 0.",
                                "hindi": "धारा, वोल्टता से π/2 से पश्चगामी होती है।\ni = i_m sin(ωt - π/2), i_m = v_m / X_L\nप्रेरण प्रतिघात: X_L = ωL (आवृत्ति पर निर्भर)\nऔसत शक्ति = 0।"
                            }
                        },
                        {
                            "id": "concept7_2_2",
                            "display_name": {
                                "english": "AC through a Capacitor",
                                "hindi": "संधारित्र में प्रत्यावर्ती धारा"
                            },
                            "description": {
                                "english": "Current leads voltage by π/2.\ni = i_m sin(ωt + π/2), i_m = v_m / X_C\nCapacitive Reactance: X_C = 1/ωC (depends on freq.)\nAverage Power = 0.",
                                "hindi": "धारा, वोल्टता से π/2 से अग्रगामी होती है।\ni = i_m sin(ωt + π/2), i_m = v_m / X_C\nधारितीय प्रतिघात: X_C = 1/ωC (आवृत्ति पर निर्भर)\nऔसत शक्ति = 0।"
                            }
                        }
                    ]
                },
                {
                    "id": "topic7_3",
                    "display_name": {
                        "english": "SERIES LCR CIRCUIT",
                        "hindi": "श्रेणी LCR परिपथ"
                    },
                    "article_range": "Section 7.6",
                    "concepts": [
                        {
                            "id": "concept7_3_1",
                            "display_name": {
                                "english": "Impedance and Phase",
                                "hindi": "प्रतिबाधा एवं कला"
                            },
                            "description": {
                                "english": "Impedance: Z = √[R² + (X_L - X_C)²]\nCurrent: i_m = v_m/Z\nPhase angle φ: tan φ = (X_L - X_C)/R\nIf X_L > X_C: φ +ve (voltage leads). If X_C > X_L: φ -ve (current leads).",
                                "hindi": "प्रतिबाधा: Z = √[R² + (X_L - X_C)²]\nधारा: i_m = v_m/Z\nकला कोण φ: tan φ = (X_L - X_C)/R\nयदि X_L > X_C: φ धनात्मक (वोल्टता अग्रगामी)। यदि X_C > X_L: φ ऋणात्मक (धारा अग्रगामी)।"
                            }
                        },
                        {
                            "id": "concept7_3_2",
                            "display_name": {
                                "english": "Resonance",
                                "hindi": "अनुनाद"
                            },
                            "description": {
                                "english": "Occurs when X_L = X_C ⇒ ω₀ = 1/√(LC).\nAt resonance: Z = R (minimum), i_m = v_m/R (maximum).\nPower factor = 1. Voltage across L and C can be very high.",
                                "hindi": "तब होता है जब X_L = X_C ⇒ ω₀ = 1/√(LC).\nअनुनाद पर: Z = R (न्यूनतम), i_m = v_m/R (अधिकतम).\nशक्ति गुणांक = 1. L एवं C के सिरों पर वोल्टता बहुत अधिक हो सकती है।"
                            }
                        }
                    ]
                },
                {
                    "id": "topic7_4",
                    "display_name": {
                        "english": "POWER IN AC CIRCUITS",
                        "hindi": "प्रत्यावर्ती धारा परिपथों में शक्ति"
                    },
                    "article_range": "Section 7.7",
                    "concepts": [
                        {
                            "id": "concept7_4_1",
                            "display_name": {
                                "english": "Power and Power Factor",
                                "hindi": "शक्ति एवं शक्ति गुणांक"
                            },
                            "description": {
                                "english": "Average Power: P = V I cos φ\ncos φ is the power factor.\nFor purely R: cos φ = 1. For L or C: cos φ = 0 (wattless current).",
                                "hindi": "औसत शक्ति: P = V I cos φ\ncos φ शक्ति गुणांक है।\nशुद्ध R के लिए: cos φ = 1. L या C के लिए: cos φ = 0 (वाटहीन धारा)।"
                            }
                        }
                    ]
                },
                {
                    "id": "topic7_5",
                    "display_name": {
                        "english": "TRANSFORMER",
                        "hindi": "ट्रांसफॉर्मर"
                    },
                    "article_range": "Section 7.8",
                    "concepts": [
                        {
                            "id": "concept7_5_1",
                            "display_name": {
                                "english": "Transformer Principle",
                                "hindi": "ट्रांसफॉर्मर का सिद्धांत"
                            },
                            "description": {
                                "english": "Based on Mutual Induction.\nVoltage Ratio: V_s/V_p = N_s/N_p\nCurrent Ratio: I_s/I_p = N_p/N_s\nStep-up: N_s > N_p; Step-down: N_s < N_p.\nEfficiency ~ 95% in ideal case.",
                                "hindi": "अन्योन्य प्रेरण पर आधारित।\nवोल्टता अनुपात: V_s/V_p = N_s/N_p\nधारा अनुपात: I_s/I_p = N_p/N_s\nउच्चायी: N_s > N_p; अपचायी: N_s < N_p.\nआदर्श स्थिति में दक्षता ~ 95%।"
                            }
                        }
                    ]
                }
            ]
        },
        # ============================================
        # CHAPTER 8: ELECTROMAGNETIC WAVES
        # ============================================
        {
            "id": "chapter8",
            "display_name": {
                "english": "CHAPTER 8: ELECTROMAGNETIC WAVES",
                "hindi": "अध्याय 8: वैद्युतचुंबकीय तरंगें"
            },
            "color": "#FFD700",
            "topics": [
                {
                    "id": "topic8_1",
                    "display_name": {
                        "english": "DISPLACEMENT CURRENT",
                        "hindi": "विस्थापन धारा"
                    },
                    "article_range": "Section 8.2",
                    "concepts": [
                        {
                            "id": "concept8_1_1",
                            "display_name": {
                                "english": "Concept of Displacement Current",
                                "hindi": "विस्थापन धारा की अवधारणा"
                            },
                            "description": {
                                "english": "Maxwell's correction to Ampere's law.\nDisplacement current: i_d = ε₀ (dΦ_E/dt)\nTotal current: i = i_c + i_d\nMaxwell's equations unify electricity and magnetism.",
                                "hindi": "एम्पियर के नियम में मैक्सवेल का संशोधन।\nविस्थापन धारा: i_d = ε₀ (dΦ_E/dt)\nकुल धारा: i = i_c + i_d\nमैक्सवेल के समीकरण विद्युत और चुंबकत्व को एकीकृत करते हैं।"
                            }
                        }
                    ]
                },
                {
                    "id": "topic8_2",
                    "display_name": {
                        "english": "ELECTROMAGNETIC WAVES",
                        "hindi": "वैद्युतचुंबकीय तरंगें"
                    },
                    "article_range": "Section 8.3",
                    "concepts": [
                        {
                            "id": "concept8_2_1",
                            "display_name": {
                                "english": "Nature of EM Waves",
                                "hindi": "वैद्युतचुंबकीय तरंगों की प्रकृति"
                            },
                            "description": {
                                "english": "Produced by accelerating charges.\nTransverse in nature: E ⟂ B ⟥ direction of propagation.\nSpeed in vacuum: c = 1/√(μ₀ε₀) = 3 x 10⁸ m/s.\nRelation: E₀/B₀ = c\nEnergy is equally shared by E and B.",
                                "hindi": "त्वरित आवेशों द्वारा उत्पन्न।\nअनुप्रस्थ प्रकृति: E ⟂ B ⟥ संचरण की दिशा।\nनिर्वात में चाल: c = 1/√(μ₀ε₀) = 3 x 10⁸ m/s.\nसंबंध: E₀/B₀ = c\nऊर्जा E एवं B में समान रूप से बँटी होती है।"
                            }
                        }
                    ]
                },
                {
                    "id": "topic8_3",
                    "display_name": {
                        "english": "ELECTROMAGNETIC SPECTRUM",
                        "hindi": "वैद्युतचुंबकीय वर्णक्रम"
                    },
                    "article_range": "Section 8.4",
                    "concepts": [
                        {
                            "id": "concept8_3_1",
                            "display_name": {
                                "english": "EM Spectrum Overview",
                                "hindi": "वैद्युतचुंबकीय वर्णक्रम अवलोकन"
                            },
                            "description": {
                                "english": "Continuous range of EM waves.\nOrder (increasing λ): γ-rays, X-rays, UV, Visible, IR, Microwaves, Radio waves.\nAll travel at speed c in vacuum.\nRegion classification based on production and detection.",
                                "hindi": "वैद्युतचुंबकीय तरंगों का सतत परिसर।\nक्रम (बढ़ते λ के अनुसार): γ-किरणें, X-किरणें, पराबैंगनी, दृश्य, अवरक्त, सूक्ष्म तरंगें, रेडियो तरंगें।\nसभी निर्वात में c चाल से चलती हैं।\nक्षेत्रों का वर्गीकरण उत्पादन एवं संसूचन पर आधारित है।"
                            }
                        },
                        {
                            "id": "concept8_3_2",
                            "display_name": {
                                "english": "Key Regions & Applications",
                                "hindi": "मुख्य क्षेत्र एवं अनुप्रयोग"
                            },
                            "description": {
                                "english": "• Radio waves: Communication\n• Microwaves: Radar, ovens\n• Infrared: Heaters, night vision\n• Visible: Vision\n• UV: Sterilization, LASIK\n• X-rays: Medical imaging\n• Gamma rays: Cancer treatment",
                                "hindi": "• रेडियो तरंगें: संचार\n• सूक्ष्म तरंगें: रडार, ओवन\n• अवरक्त: हीटर, रात्रि दृष्टि\n• दृश्य प्रकाश: दृष्टि\n• पराबैंगनी: निस्संक्रामक, लेसिक\n• X-किरणें: चिकित्सा इमेजिंग\n• गामा किरणें: कैंसर उपचार"
                            }
                        }
                    ]
                }
            ]
        },

        {
            "id": "chapter9",
            "display_name": {
                "english": "CHAPTER 9: RAY OPTICS AND OPTICAL INSTRUMENTS",
                "hindi": "अध्याय 9: किरण प्रकाशिकी एवं प्रकाशिक यंत्र"
            },
            "color": "#FF9933",
            "topics": [
                {
                    "id": "topic9_1",
                    "display_name": {
                        "english": "REFLECTION BY SPHERICAL MIRRORS",
                        "hindi": "गोलीय दर्पणों द्वारा परावर्तन"
                    },
                    "article_range": "Sections 9.2",
                    "concepts": [
                        {
                            "id": "concept9_1_1",
                            "display_name": {
                                "english": "Sign Convention",
                                "hindi": "चिह्न परिपाटी"
                            },
                            "description": {
                                "english": "• Distances measured from pole (P)\n• Direction of incident light: +ve\n• Opposite to incident light: -ve\n• Heights above axis: +ve\n• Heights below axis: -ve\n• Focal length (f): Concave (-), Convex (+)",
                                "hindi": "• दूरियाँ ध्रुव (P) से मापी जाती हैं\n• आपतित प्रकाश की दिशा: +ve\n• आपतित प्रकाश के विपरीत: -ve\n• अक्ष के ऊपर ऊँचाई: +ve\n• अक्ष के नीचे ऊँचाई: -ve\n• फोकस दूरी (f): अवतल (-), उत्तल (+)"
                            }
                        },
                        {
                            "id": "concept9_1_2",
                            "display_name": {
                                "english": "Mirror Formula",
                                "hindi": "दर्पण सूत्र"
                            },
                            "description": {
                                "english": "1/v + 1/u = 1/f\nwhere:\nu = object distance\nv = image distance\nf = focal length\nf = R/2 (R = radius of curvature)",
                                "hindi": "1/v + 1/u = 1/f\nजहाँ:\nu = वस्तु दूरी\nv = प्रतिबिंब दूरी\nf = फोकस दूरी\nf = R/2 (R = वक्रता त्रिज्या)"
                            }
                        },
                        {
                            "id": "concept9_1_3",
                            "display_name": {
                                "english": "Magnification (m)",
                                "hindi": "आवर्धन (m)"
                            },
                            "description": {
                                "english": "m = h'/h = -v/u\n• m > 1: Enlarged image\n• m < 1: Diminished image\n• m positive: Virtual, erect image\n• m negative: Real, inverted image",
                                "hindi": "m = h'/h = -v/u\n• m > 1: बड़ा प्रतिबिंब\n• m < 1: छोटा प्रतिबिंब\n• m धनात्मक: आभासी, सीधा प्रतिबिंब\n• m ऋणात्मक: वास्तविक, उल्टा प्रतिबिंब"
                            }
                        }
                    ]
                },
                {
                    "id": "topic9_2",
                    "display_name": {
                        "english": "REFRACTION",
                        "hindi": "अपवर्तन"
                    },
                    "article_range": "Sections 9.3-9.4",
                    "concepts": [
                        {
                            "id": "concept9_2_1",
                            "display_name": {
                                "english": "Snell's Law",
                                "hindi": "स्नेल का नियम"
                            },
                            "description": {
                                "english": "n₁ sin i = n₂ sin r\nRefractive index: n = c/v\nRelative refractive index: n₂₁ = n₂/n₁ = v₁/v₂",
                                "hindi": "n₁ sin i = n₂ sin r\nअपवर्तनांक: n = c/v\nआपेक्षिक अपवर्तनांक: n₂₁ = n₂/n₁ = v₁/v₂"
                            }
                        },
                        {
                            "id": "concept9_2_2",
                            "display_name": {
                                "english": "Total Internal Reflection",
                                "hindi": "पूर्ण आंतरिक परावर्तन"
                            },
                            "description": {
                                "english": "Critical angle: sin i_c = n₂/n₁ (n₁ > n₂)\nFor i > i_c, TIR occurs\nApplications: Optical fibres, prisms\nDiamond's sparkle due to TIR",
                                "hindi": "क्रांतिक कोण: sin i_c = n₂/n₁ (n₁ > n₂)\ni > i_c के लिए, पूर्ण आंतरिक परावर्तन\nअनुप्रयोग: प्रकाशित तंतु, प्रिज्म\nहीरे की चमक पूर्ण आंतरिक परावर्तन के कारण"
                            }
                        }
                    ]
                },
                {
                    "id": "topic9_3",
                    "display_name": {
                        "english": "REFRACTION BY LENSES",
                        "hindi": "लेंसों द्वारा अपवर्तन"
                    },
                    "article_range": "Sections 9.5",
                    "concepts": [
                        {
                            "id": "concept9_3_1",
                            "display_name": {
                                "english": "Lens Maker's Formula",
                                "hindi": "लेंस निर्माता सूत्र"
                            },
                            "description": {
                                "english": "1/f = (n₂₁ - 1)(1/R₁ - 1/R₂)\nwhere:\nn₂₁ = refractive index of lens material w.r.t. medium\nR₁, R₂ = radii of curvature",
                                "hindi": "1/f = (n₂₁ - 1)(1/R₁ - 1/R₂)\nजहाँ:\nn₂₁ = माध्यम के सापेक्ष लेंस पदार्थ का अपवर्तनांक\nR₁, R₂ = वक्रता त्रिज्याएँ"
                            }
                        },
                        {
                            "id": "concept9_3_2",
                            "display_name": {
                                "english": "Lens Formula",
                                "hindi": "लेंस सूत्र"
                            },
                            "description": {
                                "english": "1/v - 1/u = 1/f\nMagnification: m = v/u\nPower of lens: P = 1/f (in metres)\nUnit: Dioptre (D)",
                                "hindi": "1/v - 1/u = 1/f\nआवर्धन: m = v/u\nलेंस की क्षमता: P = 1/f (मीटर में)\nमात्रक: डाइऑप्टर (D)"
                            }
                        },
                        {
                            "id": "concept9_3_3",
                            "display_name": {
                                "english": "Combination of Lenses",
                                "hindi": "लेंसों का संयोजन"
                            },
                            "description": {
                                "english": "For lenses in contact:\n1/F = 1/f₁ + 1/f₂ + 1/f₃ + ...\nP = P₁ + P₂ + P₃ + ...",
                                "hindi": "संपर्क में रखे लेंसों के लिए:\n1/F = 1/f₁ + 1/f₂ + 1/f₃ + ...\nP = P₁ + P₂ + P₃ + ..."
                            }
                        }
                    ]
                },
                {
                    "id": "topic9_4",
                    "display_name": {
                        "english": "REFRACTION THROUGH PRISM",
                        "hindi": "प्रिज्म से अपवर्तन"
                    },
                    "article_range": "Section 9.6",
                    "concepts": [
                        {
                            "id": "concept9_4_1",
                            "display_name": {
                                "english": "Prism Formula",
                                "hindi": "प्रिज्म सूत्र"
                            },
                            "description": {
                                "english": "δ = i + e - A\nwhere:\nδ = angle of deviation\ni = angle of incidence\ne = angle of emergence\nA = angle of prism\nr₁ + r₂ = A",
                                "hindi": "δ = i + e - A\nजहाँ:\nδ = विचलन कोण\ni = आपतन कोण\ne = निर्गमन कोण\nA = प्रिज्म कोण\nr₁ + r₂ = A"
                            }
                        },
                        {
                            "id": "concept9_4_2",
                            "display_name": {
                                "english": "Minimum Deviation",
                                "hindi": "न्यूनतम विचलन"
                            },
                            "description": {
                                "english": "At minimum deviation (δ_m):\ni = e, r₁ = r₂ = A/2\nRefractive index:\nn = sin[(A + δ_m)/2] / sin(A/2)\nFor thin prism: δ_m = (n-1)A",
                                "hindi": "न्यूनतम विचलन (δ_m) पर:\ni = e, r₁ = r₂ = A/2\nअपवर्तनांक:\nn = sin[(A + δ_m)/2] / sin(A/2)\nपतले प्रिज्म के लिए: δ_m = (n-1)A"
                            }
                        },
                        {
                            "id": "concept9_4_3",
                            "display_name": {
                                "english": "Dispersion",
                                "hindi": "वर्ण-विक्षेपण"
                            },
                            "description": {
                                "english": "Splitting of white light into VIBGYOR\nAngular dispersion = δ_v - δ_r\nDispersive power = (δ_v - δ_r)/δ_y\nCause: Different n for different colours",
                                "hindi": "श्वेत प्रकाश का VIBGYOR रंगों में विभाजन\nकोणीय वर्ण-विक्षेपण = δ_v - δ_r\nवर्ण-विक्षेपण क्षमता = (δ_v - δ_r)/δ_y\nकारण: विभिन्न रंगों के लिए n भिन्न"
                            }
                        }
                    ]
                },
                {
                    "id": "topic9_5",
                    "display_name": {
                        "english": "OPTICAL INSTRUMENTS",
                        "hindi": "प्रकाशिक यंत्र"
                    },
                    "article_range": "Section 9.7",
                    "concepts": [
                        {
                            "id": "concept9_5_1",
                            "display_name": {
                                "english": "Simple Microscope",
                                "hindi": "सरल सूक्ष्मदर्शी"
                            },
                            "description": {
                                "english": "Magnifying power:\n• Image at near point: m = 1 + D/f\n• Image at infinity: m = D/f\nwhere D = 25 cm (least distance of distinct vision)",
                                "hindi": "आवर्धन क्षमता:\n• निकट बिंदु पर प्रतिबिंब: m = 1 + D/f\n• अनंत पर प्रतिबिंब: m = D/f\nजहाँ D = 25 सेमी (स्पष्ट दर्शन की न्यूनतम दूरी)"
                            }
                        },
                        {
                            "id": "concept9_5_2",
                            "display_name": {
                                "english": "Compound Microscope",
                                "hindi": "संयुक्त सूक्ष्मदर्शी"
                            },
                            "description": {
                                "english": "Total magnification: m = m₀ × m_e\nm₀ = v₀/|u₀| (objective)\nm_e = 1 + D/f_e (eyepiece)\nApprox: m = (L/f₀) × (D/f_e)\nL = tube length",
                                "hindi": "कुल आवर्धन: m = m₀ × m_e\nm₀ = v₀/|u₀| (अभिदृश्यक)\nm_e = 1 + D/f_e (नेत्रिका)\nलगभग: m = (L/f₀) × (D/f_e)\nL = नलिका की लंबाई"
                            }
                        },
                        {
                            "id": "concept9_5_3",
                            "display_name": {
                                "english": "Astronomical Telescope",
                                "hindi": "खगोलीय दूरदर्शी"
                            },
                            "description": {
                                "english": "Magnifying power:\n• Normal adjustment: m = -f₀/f_e\n• Image at near point: m = -(f₀/f_e)(1 + f_e/D)\nLength of telescope = f₀ + f_e\nReflecting telescopes use mirrors",
                                "hindi": "आवर्धन क्षमता:\n• सामान्य समायोजन: m = -f₀/f_e\n• निकट बिंदु पर प्रतिबिंब: m = -(f₀/f_e)(1 + f_e/D)\nदूरदर्शी की लंबाई = f₀ + f_e\nपरावर्ती दूरदर्शी दर्पणों का उपयोग करते हैं"
                            }
                        }
                    ]
                }
            ]
        },
        # ============================================
        # CHAPTER 10: WAVE OPTICS
        # ============================================
        {
            "id": "chapter10",
            "display_name": {
                "english": "CHAPTER 10: WAVE OPTICS",
                "hindi": "अध्याय 10: तरंग प्रकाशिकी"
            },
            "color": "#0066CC",
            "topics": [
                {
                    "id": "topic10_1",
                    "display_name": {
                        "english": "HUYGENS PRINCIPLE",
                        "hindi": "हाइगेंस का सिद्धांत"
                    },
                    "article_range": "Sections 10.2-10.3",
                    "concepts": [
                        {
                            "id": "concept10_1_1",
                            "display_name": {
                                "english": "Wavefront and Huygens Principle",
                                "hindi": "तरंगाग्र एवं हाइगेंस सिद्धांत"
                            },
                            "description": {
                                "english": "Wavefront: Locus of points in same phase\nHuygens Principle: Each point on wavefront acts as secondary source\nNew wavefront = envelope of secondary wavelets",
                                "hindi": "तरंगाग्र: समान कला वाले बिंदुओं का बिंदुपथ\nहाइगेंस सिद्धांत: तरंगाग्र पर प्रत्येक बिंदु द्वितीयक स्रोत\nनया तरंगाग्र = द्वितीयक तरंगिकाओं का आवरण"
                            }
                        },
                        {
                            "id": "concept10_1_2",
                            "display_name": {
                                "english": "Reflection using Huygens Principle",
                                "hindi": "हाइगेंस सिद्धांत से परावर्तन"
                            },
                            "description": {
                                "english": "Laws of reflection derived:\nAngle of incidence = Angle of reflection\nIncident, reflected, normal in same plane",
                                "hindi": "परावर्तन के नियम व्युत्पन्न:\nआपतन कोण = परावर्तन कोण\nआपतित, परावर्तित किरण एवं अभिलंब एक ही तल में"
                            }
                        },
                        {
                            "id": "concept10_1_3",
                            "display_name": {
                                "english": "Refraction using Huygens Principle",
                                "hindi": "हाइगेंस सिद्धांत से अपवर्तन"
                            },
                            "description": {
                                "english": "Snell's law derived: sin i/sin r = v₁/v₂ = n₂/n₁\nWave theory predicts v₂ < v₁ when ray bends towards normal\nSpeed of light is less in denser medium",
                                "hindi": "स्नेल का नियम व्युत्पन्न: sin i/sin r = v₁/v₂ = n₂/n₁\nतरंग सिद्धांत भविष्यवाणी: जब किरण अभिलंब की ओर झुकती है तो v₂ < v₁\nसघन माध्यम में प्रकाश की चाल कम होती है"
                            }
                        }
                    ]
                },
                {
                    "id": "topic10_2",
                    "display_name": {
                        "english": "INTERFERENCE",
                        "hindi": "व्यतिकरण"
                    },
                    "article_range": "Sections 10.4-10.5",
                    "concepts": [
                        {
                            "id": "concept10_2_1",
                            "display_name": {
                                "english": "Coherent Sources",
                                "hindi": "संबद्ध स्रोत"
                            },
                            "description": {
                                "english": "Sources with constant phase difference\nProduced by division of wavefront (Young's double slit)\nIncoherent sources: Random phase, no stable pattern",
                                "hindi": "स्थिर कला अंतर वाले स्रोत\nतरंगाग्र विभाजन से उत्पन्न (यंग का द्वि-झिर्री प्रयोग)\nअसंबद्ध स्रोत: यादृच्छिक कला, कोई स्थिर प्रतिरूप नहीं"
                            }
                        },
                        {
                            "id": "concept10_2_2",
                            "display_name": {
                                "english": "Young's Double Slit Experiment",
                                "hindi": "यंग का द्वि-झिर्री प्रयोग"
                            },
                            "description": {
                                "english": "Path difference: Δx = yd/D\nFor maxima: Δx = nλ (n = 0,1,2...)\nFor minima: Δx = (2n-1)λ/2\nFringe width: β = λD/d\nIntensity: I = 4I₀ cos²(φ/2)",
                                "hindi": "पथांतर: Δx = yd/D\nदीप्त फ्रिंज के लिए: Δx = nλ (n = 0,1,2...)\nअदीप्त फ्रिंज के लिए: Δx = (2n-1)λ/2\nफ्रिंज चौड़ाई: β = λD/d\nतीव्रता: I = 4I₀ cos²(φ/2)"
                            }
                        },
                        {
                            "id": "concept10_2_3",
                            "display_name": {
                                "english": "Conditions for Interference",
                                "hindi": "व्यतिकरण की शर्तें"
                            },
                            "description": {
                                "english": "• Sources must be coherent\n• Same frequency and wavelength\n• Amplitudes should be nearly equal\n• Path difference should not exceed coherence length",
                                "hindi": "• स्रोत संबद्ध होने चाहिए\n• समान आवृत्ति एवं तरंगदैर्घ्य\n• आयाम लगभग समान होने चाहिए\n• पथांतर संबद्धता लंबाई से अधिक न हो"
                            }
                        }
                    ]
                },
                {
                    "id": "topic10_3",
                    "display_name": {
                        "english": "DIFFRACTION",
                        "hindi": "विवर्तन"
                    },
                    "article_range": "Section 10.6",
                    "concepts": [
                        {
                            "id": "concept10_3_1",
                            "display_name": {
                                "english": "Single Slit Diffraction",
                                "hindi": "एकल झिर्री विवर्तन"
                            },
                            "description": {
                                "english": "For minima: a sinθ = nλ (n = ±1, ±2...)\nCentral maximum: at θ = 0\nWidth of central max = 2λD/a\nIntensity falls rapidly for secondary maxima",
                                "hindi": "अदीप्त के लिए: a sinθ = nλ (n = ±1, ±2...)\nकेंद्रीय दीप्त: θ = 0 पर\nकेंद्रीय दीप्त की चौड़ाई = 2λD/a\nद्वितीयक दीप्तों की तीव्रता तेजी से घटती है"
                            }
                        },
                        {
                            "id": "concept10_3_2",
                            "display_name": {
                                "english": "Diffraction vs Interference",
                                "hindi": "विवर्तन बनाम व्यतिकरण"
                            },
                            "description": {
                                "english": "Interference: Superposition of few waves\nDiffraction: Superposition of continuous waves\nBoth redistribute energy, obey conservation",
                                "hindi": "व्यतिकरण: कुछ तरंगों का अध्यारोपण\nविवर्तन: सतत तरंगों का अध्यारोपण\nदोनों में ऊर्जा पुनर्वितरित होती है, संरक्षण का पालन"
                            }
                        }
                    ]
                },
                {
                    "id": "topic10_4",
                    "display_name": {
                        "english": "POLARISATION",
                        "hindi": "ध्रुवण"
                    },
                    "article_range": "Section 10.7",
                    "concepts": [
                        {
                            "id": "concept10_4_1",
                            "display_name": {
                                "english": "Polarisation of Light",
                                "hindi": "प्रकाश का ध्रुवण"
                            },
                            "description": {
                                "english": "Light waves are transverse\nUnpolarised light: E vector in all directions\nPolarised light: E vector in one direction\nOnly transverse waves can be polarised",
                                "hindi": "प्रकाश तरंगें अनुप्रस्थ होती हैं\nअध्रुवित प्रकाश: E सदिश सभी दिशाओं में\nध्रुवित प्रकाश: E सदिश एक दिशा में\nकेवल अनुप्रस्थ तरंगें ही ध्रुवित हो सकती हैं"
                            }
                        },
                        {
                            "id": "concept10_4_2",
                            "display_name": {
                                "english": "Malus' Law",
                                "hindi": "मैलस का नियम"
                            },
                            "description": {
                                "english": "I = I₀ cos²θ\nwhere θ is angle between polariser and analyser\nWhen θ = 0°, I = I₀ (max)\nWhen θ = 90°, I = 0 (min)",
                                "hindi": "I = I₀ cos²θ\nजहाँ θ ध्रुवक एवं विश्लेषक के मध्य कोण है\nθ = 0° पर, I = I₀ (अधिकतम)\nθ = 90° पर, I = 0 (न्यूनतम)"
                            }
                        },
                        {
                            "id": "concept10_4_3",
                            "display_name": {
                                "english": "Polarisation by Reflection",
                                "hindi": "परावर्तन द्वारा ध्रुवण"
                            },
                            "description": {
                                "english": "Brewster's Law: tan i_B = n\nAt Brewster angle, reflected light is completely polarised\nReflected and refracted rays are perpendicular\ni_B + r = 90°",
                                "hindi": "बूस्टर का नियम: tan i_B = n\nबूस्टर कोण पर, परावर्तित प्रकाश पूर्णतः ध्रुवित होता है\nपरावर्तित एवं अपवर्तित किरणें लंबवत होती हैं\ni_B + r = 90°"
                            }
                        }
                    ]
                }
            ]
        },
        # ============================================
        # CHAPTER 11: DUAL NATURE OF RADIATION AND MATTER
        # ============================================
        {
            "id": "chapter11",
            "display_name": {
                "english": "CHAPTER 11: DUAL NATURE OF RADIATION AND MATTER",
                "hindi": "अध्याय 11: विकिरण तथा द्रव्य की द्वैत प्रकृति"
            },
            "color": "#138808",
            "topics": [
                {
                    "id": "topic11_1",
                    "display_name": {
                        "english": "PHOTOELECTRIC EFFECT",
                        "hindi": "प्रकाश विद्युत प्रभाव"
                    },
                    "article_range": "Sections 11.2-11.4",
                    "concepts": [
                        {
                            "id": "concept11_1_1",
                            "display_name": {
                                "english": "Electron Emission",
                                "hindi": "इलेक्ट्रॉन उत्सर्जन"
                            },
                            "description": {
                                "english": "Work function (φ₀): Min energy to eject electron\nThermionic emission: Heating\nField emission: Strong electric field\nPhotoelectric emission: Light of suitable frequency",
                                "hindi": "कार्य फलन (φ₀): इलेक्ट्रॉन उत्सर्जन के लिए न्यूनतम ऊर्जा\nतापायनिक उत्सर्जन: तापन\nक्षेत्र उत्सर्जन: प्रबल विद्युत क्षेत्र\nप्रकाश विद्युत उत्सर्जन: उपयुक्त आवृत्ति का प्रकाश"
                            }
                        },
                        {
                            "id": "concept11_1_2",
                            "display_name": {
                                "english": "Experimental Observations",
                                "hindi": "प्रायोगिक प्रेक्षण"
                            },
                            "description": {
                                "english": "• No emission below threshold frequency ν₀\n• K_max independent of intensity, depends on ν\n• Photocurrent ∝ intensity\n• Instantaneous emission (∼10⁻⁹ s)\nStopping potential V₀ = K_max/e",
                                "hindi": "• देहली आवृत्ति ν₀ के नीचे कोई उत्सर्जन नहीं\n• K_max तीव्रता से स्वतंत्र, ν पर निर्भर\n• प्रकाश धारा ∝ तीव्रता\n• तात्कालिक उत्सर्जन (∼10⁻⁹ s)\nनिरोधी विभव V₀ = K_max/e"
                            }
                        }
                    ]
                },
                {
                    "id": "topic11_2",
                    "display_name": {
                        "english": "EINSTEIN'S PHOTOELECTRIC EQUATION",
                        "hindi": "आइंस्टीन का प्रकाश विद्युत समीकरण"
                    },
                    "article_range": "Sections 11.5-11.7",
                    "concepts": [
                        {
                            "id": "concept11_2_1",
                            "display_name": {
                                "english": "Photon Picture",
                                "hindi": "फोटॉन चित्र"
                            },
                            "description": {
                                "english": "Light consists of photons, each with energy E = hν\nPhoton momentum: p = h/λ = hν/c\nIntensity ∝ number of photons\nPhoton has zero rest mass",
                                "hindi": "प्रकाश फोटॉनों से बना है, प्रत्येक की ऊर्जा E = hν\nफोटॉन संवेग: p = h/λ = hν/c\nतीव्रता ∝ फोटॉनों की संख्या\nफोटॉन का विराम द्रव्यमान शून्य"
                            }
                        },
                        {
                            "id": "concept11_2_2",
                            "display_name": {
                                "english": "Einstein's Equation",
                                "hindi": "आइंस्टीन का समीकरण"
                            },
                            "description": {
                                "english": "K_max = hν - φ₀\neV₀ = hν - φ₀\nThreshold frequency: ν₀ = φ₀/h\nSlope of V₀ vs ν graph = h/e\nh = 6.63 × 10⁻³⁴ Js",
                                "hindi": "K_max = hν - φ₀\neV₀ = hν - φ₀\nदेहली आवृत्ति: ν₀ = φ₀/h\nV₀ बनाम ν ग्राफ की ढाल = h/e\nh = 6.63 × 10⁻³⁴ Js"
                            }
                        }
                    ]
                },
                {
                    "id": "topic11_3",
                    "display_name": {
                        "english": "WAVE NATURE OF MATTER",
                        "hindi": "द्रव्य की तरंग प्रकृति"
                    },
                    "article_range": "Section 11.8",
                    "concepts": [
                        {
                            "id": "concept11_3_1",
                            "display_name": {
                                "english": "de Broglie Hypothesis",
                                "hindi": "डी ब्रोग्ली परिकल्पना"
                            },
                            "description": {
                                "english": "λ = h/p = h/mv\nMatter waves associated with moving particles\nDual nature: Both particle and wave properties\nValid for all particles (electron, proton, etc.)",
                                "hindi": "λ = h/p = h/mv\nगतिमान कणों से संबद्ध द्रव्य तरंगें\nद्वैत प्रकृति: कण एवं तरंग दोनों गुण\nसभी कणों के लिए मान्य (इलेक्ट्रॉन, प्रोटॉन, आदि)"
                            }
                        },
                        {
                            "id": "concept11_3_2",
                            "display_name": {
                                "english": "Davisson-Germer Experiment",
                                "hindi": "डेविसन-जर्मर प्रयोग"
                            },
                            "description": {
                                "english": "Confirmed wave nature of electrons\nElectron diffraction from Ni crystal\nVerified de Broglie relation\nWavelength matches λ = h/√(2meV)",
                                "hindi": "इलेक्ट्रॉनों की तरंग प्रकृति की पुष्टि\nNi क्रिस्टल से इलेक्ट्रॉन विवर्तन\nडी ब्रोग्ली संबंध की पुष्टि\nतरंगदैर्घ्य λ = h/√(2meV) से मेल खाता है"
                            }
                        }
                    ]
                }
            ]
        },
        # ============================================
        # CHAPTER 12: ATOMS
        # ============================================
        {
            "id": "chapter12",
            "display_name": {
                "english": "CHAPTER 12: ATOMS",
                "hindi": "अध्याय 12: परमाणु"
            },
            "color": "#FFD700",
            "topics": [
                {
                    "id": "topic12_1",
                    "display_name": {
                        "english": "RUTHERFORD'S NUCLEAR MODEL",
                        "hindi": "रदरफोर्ड का नाभिकीय मॉडल"
                    },
                    "article_range": "Sections 12.2",
                    "concepts": [
                        {
                            "id": "concept12_1_1",
                            "display_name": {
                                "english": "Alpha Particle Scattering",
                                "hindi": "अल्फा कण प्रकीर्णन"
                            },
                            "description": {
                                "english": "Most α particles pass through foil\nFew scatter by large angles\nNucleus: small, dense, positively charged\nSize of nucleus ∼ 10⁻¹⁴ to 10⁻¹⁵ m",
                                "hindi": "अधिकांश α कण पन्नी से निकल जाते हैं\nकुछ बड़े कोणों पर प्रकीर्णित होते हैं\nनाभिक: छोटा, सघन, धनावेशित\nनाभिक का आकार ∼ 10⁻¹⁴ से 10⁻¹⁵ m"
                            }
                        },
                        {
                            "id": "concept12_1_2",
                            "display_name": {
                                "english": "Distance of Closest Approach",
                                "hindi": "निकटतम पहुँच दूरी"
                            },
                            "description": {
                                "english": "r₀ = (1/4πε₀) × (2Ze²)/(K)\nwhere K = initial KE of α particle\nAt r₀, KE = 0, total energy = PE\nGives upper limit of nuclear size",
                                "hindi": "r₀ = (1/4πε₀) × (2Ze²)/(K)\nजहाँ K = α कण की प्रारंभिक गतिज ऊर्जा\nr₀ पर, KE = 0, कुल ऊर्जा = स्थितिज ऊर्जा\nनाभिकीय आकार की ऊपरी सीमा देता है"
                            }
                        }
                    ]
                },
                {
                    "id": "topic12_2",
                    "display_name": {
                        "english": "BOHR'S MODEL OF HYDROGEN ATOM",
                        "hindi": "हाइड्रोजन परमाणु का बोर मॉडल"
                    },
                    "article_range": "Sections 12.4",
                    "concepts": [
                        {
                            "id": "concept12_2_1",
                            "display_name": {
                                "english": "Bohr's Postulates",
                                "hindi": "बोर के अभिगृहीत"
                            },
                            "description": {
                                "english": "1. Electrons in stationary orbits (no radiation)\n2. Angular momentum quantisation: L = nh/2π\n3. Radiation during transition: hν = E_i - E_f",
                                "hindi": "1. इलेक्ट्रॉन स्थिर कक्षाओं में (विकिरण नहीं)\n2. कोणीय संवेग क्वांटीकरण: L = nh/2π\n3. संक्रमण के दौरान विकिरण: hν = E_i - E_f"
                            }
                        },
                        {
                            "id": "concept12_2_2",
                            "display_name": {
                                "english": "Bohr's Radius and Energy",
                                "hindi": "बोर त्रिज्या एवं ऊर्जा"
                            },
                            "description": {
                                "english": "r_n = n² × a₀, where a₀ = 0.529 Å\nE_n = -13.6/n² eV\nv_n = (c/137) × (1/n)\nEnergy of ground state (n=1) = -13.6 eV",
                                "hindi": "r_n = n² × a₀, जहाँ a₀ = 0.529 Å\nE_n = -13.6/n² eV\nv_n = (c/137) × (1/n)\nनिम्नतम ऊर्जा स्तर (n=1) की ऊर्जा = -13.6 eV"
                            }
                        },
                        {
                            "id": "concept12_2_3",
                            "display_name": {
                                "english": "Spectral Series of Hydrogen",
                                "hindi": "हाइड्रोजन की स्पेक्ट्रमी श्रेणियाँ"
                            },
                            "description": {
                                "english": "1/λ = R(1/n_f² - 1/n_i²), R = 1.097 × 10⁷ m⁻¹\nLyman: n_f = 1 (UV)\nBalmer: n_f = 2 (Visible)\nPaschen: n_f = 3 (IR)\nBrackett: n_f = 4 (IR)\nPfund: n_f = 5 (IR)",
                                "hindi": "1/λ = R(1/n_f² - 1/n_i²), R = 1.097 × 10⁷ m⁻¹\nलाइमन: n_f = 1 (पराबैंगनी)\nबामर: n_f = 2 (दृश्य)\nपाश्चन: n_f = 3 (अवरक्त)\nब्रेकेट: n_f = 4 (अवरक्त)\nफुंड: n_f = 5 (अवरक्त)"
                            }
                        }
                    ]
                },
                {
                    "id": "topic12_3",
                    "display_name": {
                        "english": "DE BROGLIE'S EXPLANATION",
                        "hindi": "डी ब्रोग्ली की व्याख्या"
                    },
                    "article_range": "Section 12.6",
                    "concepts": [
                        {
                            "id": "concept12_3_1",
                            "display_name": {
                                "english": "Wave Nature and Quantisation",
                                "hindi": "तरंग प्रकृति एवं क्वांटीकरण"
                            },
                            "description": {
                                "english": "Standing wave condition: 2πr_n = nλ\nλ = h/mv ⇒ mvr_n = nh/2π\nExplains Bohr's quantisation postulate\nElectron wave must fit exactly in orbit",
                                "hindi": "अप्रगामी तरंग शर्त: 2πr_n = nλ\nλ = h/mv ⇒ mvr_n = nh/2π\nबोर के क्वांटीकरण अभिगृहीत की व्याख्या\nइलेक्ट्रॉन तरंग कक्षा में बिल्कुल फिट होनी चाहिए"
                            }
                        }
                    ]
                }
            ]
        },
        # ============================================
        # CHAPTER 13: NUCLEI
        # ============================================
        {
            "id": "chapter13",
            "display_name": {
                "english": "CHAPTER 13: NUCLEI",
                "hindi": "अध्याय 13: नाभिक"
            },
            "color": "#FF9933",
            "topics": [
                {
                    "id": "topic13_1",
                    "display_name": {
                        "english": "NUCLEAR PROPERTIES",
                        "hindi": "नाभिकीय गुण"
                    },
                    "article_range": "Sections 13.2-13.3",
                    "concepts": [
                        {
                            "id": "concept13_1_1",
                            "display_name": {
                                "english": "Nuclear Composition",
                                "hindi": "नाभिकीय संघटन"
                            },
                            "description": {
                                "english": "Nucleus: Protons + Neutrons\nAtomic number Z = number of protons\nMass number A = Z + N (N = neutrons)\nIsotopes: Same Z, different A\nIsobars: Same A, different Z\nIsotones: Same N, different Z",
                                "hindi": "नाभिक: प्रोटॉन + न्यूट्रॉन\nपरमाणु क्रमांक Z = प्रोटॉनों की संख्या\nद्रव्यमान संख्या A = Z + N (N = न्यूट्रॉन)\nसमस्थानिक: समान Z, भिन्न A\nसमभारिक: समान A, भिन्न Z\nसमन्यूट्रॉनिक: समान N, भिन्न Z"
                            }
                        },
                        {
                            "id": "concept13_1_2",
                            "display_name": {
                                "english": "Nuclear Size and Density",
                                "hindi": "नाभिकीय आकार एवं घनत्व"
                            },
                            "description": {
                                "english": "R = R₀A¹/³, R₀ = 1.2 × 10⁻¹⁵ m\nNuclear volume ∝ A\nNuclear density ≈ 2.3 × 10¹⁷ kg/m³\nIndependent of A (constant)",
                                "hindi": "R = R₀A¹/³, R₀ = 1.2 × 10⁻¹⁵ m\nनाभिकीय आयतन ∝ A\nनाभिकीय घनत्व ≈ 2.3 × 10¹⁷ kg/m³\nA से स्वतंत्र (स्थिर)"
                            }
                        },
                        {
                            "id": "concept13_1_3",
                            "display_name": {
                                "english": "Atomic Mass Unit",
                                "hindi": "परमाणु द्रव्यमान इकाई"
                            },
                            "description": {
                                "english": "1 u = 1/12 mass of ¹²C atom\n1 u = 1.6605 × 10⁻²⁷ kg\nMass-energy equivalence: 1 u = 931.5 MeV/c²\nm_p = 1.00727 u, m_n = 1.00866 u",
                                "hindi": "1 u = ¹²C परमाणु के द्रव्यमान का 1/12\n1 u = 1.6605 × 10⁻²⁷ kg\nद्रव्यमान-ऊर्जा तुल्यता: 1 u = 931.5 MeV/c²\nm_p = 1.00727 u, m_n = 1.00866 u"
                            }
                        }
                    ]
                },
                {
                    "id": "topic13_2",
                    "display_name": {
                        "english": "BINDING ENERGY",
                        "hindi": "बंधन ऊर्जा"
                    },
                    "article_range": "Section 13.4",
                    "concepts": [
                        {
                            "id": "concept13_2_1",
                            "display_name": {
                                "english": "Mass Defect and Binding Energy",
                                "hindi": "द्रव्यमान क्षति एवं बंधन ऊर्जा"
                            },
                            "description": {
                                "english": "Mass defect: Δm = [Zm_p + (A-Z)m_n] - M\nBinding energy: E_b = Δm × c²\nE_b = Δm (in u) × 931.5 MeV\nBinding energy per nucleon = E_b/A",
                                "hindi": "द्रव्यमान क्षति: Δm = [Zm_p + (A-Z)m_n] - M\nबंधन ऊर्जा: E_b = Δm × c²\nE_b = Δm (u में) × 931.5 MeV\nप्रति न्यूक्लिऑन बंधन ऊर्जा = E_b/A"
                            }
                        },
                        {
                            "id": "concept13_2_2",
                            "display_name": {
                                "english": "Binding Energy Curve",
                                "hindi": "बंधन ऊर्जा वक्र"
                            },
                            "description": {
                                "english": "Max at A≈56 (Fe): ~8.8 MeV/nucleon\nLower for light and heavy nuclei\nFusion: Light nuclei combine (energy released)\nFission: Heavy nuclei split (energy released)",
                                "hindi": "अधिकतम A≈56 (Fe) पर: ~8.8 MeV/न्यूक्लिऑन\nहल्के एवं भारी नाभिकों के लिए कम\nसंलयन: हल्के नाभिक संयुक्त होते हैं (ऊर्जा मुक्त)\nविखंडन: भारी नाभिक टूटते हैं (ऊर्जा मुक्त)"
                            }
                        }
                    ]
                },
                {
                    "id": "topic13_3",
                    "display_name": {
                        "english": "RADIOACTIVITY",
                        "hindi": "रेडियोधर्मिता"
                    },
                    "article_range": "Section 13.6",
                    "concepts": [
                        {
                            "id": "concept13_3_1",
                            "display_name": {
                                "english": "Types of Decay",
                                "hindi": "क्षय के प्रकार"
                            },
                            "description": {
                                "english": "α-decay: ⁴₂He nucleus emitted\nβ⁻-decay: n → p + e⁻ + ν̄ (antineutrino)\nβ⁺-decay: p → n + e⁺ + ν (neutrino)\nγ-decay: High energy photons",
                                "hindi": "α-क्षय: ⁴₂He नाभिक उत्सर्जित\nβ⁻-क्षय: n → p + e⁻ + ν̄ (प्रतिन्यूट्रिनो)\nβ⁺-क्षय: p → n + e⁺ + ν (न्यूट्रिनो)\nγ-क्षय: उच्च ऊर्जा फोटॉन"
                            }
                        },
                        {
                            "id": "concept13_3_2",
                            "display_name": {
                                "english": "Radioactive Decay Law",
                                "hindi": "रेडियोधर्मी क्षय नियम"
                            },
                            "description": {
                                "english": "dN/dt = -λN\nN = N₀e⁻λt\nHalf-life: T₁/₂ = ln2/λ = 0.693/λ\nMean life: τ = 1/λ = 1.44 T₁/₂\nActivity: R = λN = R₀e⁻λt",
                                "hindi": "dN/dt = -λN\nN = N₀e⁻λt\nअर्धायु काल: T₁/₂ = ln2/λ = 0.693/λ\nमाध्य आयु: τ = 1/λ = 1.44 T₁/₂\nसक्रियता: R = λN = R₀e⁻λt"
                            }
                        }
                    ]
                },
                {
                    "id": "topic13_4",
                    "display_name": {
                        "english": "NUCLEAR ENERGY",
                        "hindi": "नाभिकीय ऊर्जा"
                    },
                    "article_range": "Section 13.7",
                    "concepts": [
                        {
                            "id": "concept13_4_1",
                            "display_name": {
                                "english": "Nuclear Fission",
                                "hindi": "नाभिकीय विखंडन"
                            },
                            "description": {
                                "english": "n + ²³⁵U → ¹⁴¹Ba + ⁹²Kr + 3n + 200 MeV\nChain reaction\nCritical mass\nControlled in nuclear reactors\nUncontrolled in atom bomb",
                                "hindi": "n + ²³⁵U → ¹⁴¹Ba + ⁹²Kr + 3n + 200 MeV\nश्रृंखला अभिक्रिया\nक्रांतिक द्रव्यमान\nनाभिकीय रिएक्टरों में नियंत्रित\nपरमाणु बम में अनियंत्रित"
                            }
                        },
                        {
                            "id": "concept13_4_2",
                            "display_name": {
                                "english": "Nuclear Fusion",
                                "hindi": "नाभिकीय संलयन"
                            },
                            "description": {
                                "english": "Light nuclei combine to form heavier nucleus\nRequires high temperature (∼10⁷ K)\nSource of energy in stars (sun)\n4¹H → ⁴He + 2e⁺ + 2ν + 26.7 MeV\nTokamak: Fusion reactor research",
                                "hindi": "हल्के नाभिक मिलकर भारी नाभिक बनाते हैं\nउच्च तापमान की आवश्यकता (∼10⁷ K)\nतारों में ऊर्जा का स्रोत (सूर्य)\n4¹H → ⁴He + 2e⁺ + 2ν + 26.7 MeV\nटोकामक: संलयन रिएक्टर अनुसंधान"
                            }
                        }
                    ]
                }
            ]
        },
        # ============================================
        # CHAPTER 14: SEMICONDUCTOR ELECTRONICS
        # ============================================
        {
            "id": "chapter14",
            "display_name": {
                "english": "CHAPTER 14: SEMICONDUCTOR ELECTRONICS",
                "hindi": "अध्याय 14: अर्धचालक इलेक्ट्रॉनिकी"
            },
            "color": "#0066CC",
            "topics": [
                {
                    "id": "topic14_1",
                    "display_name": {
                        "english": "CLASSIFICATION OF MATERIALS",
                        "hindi": "पदार्थों का वर्गीकरण"
                    },
                    "article_range": "Sections 14.2",
                    "concepts": [
                        {
                            "id": "concept14_1_1",
                            "display_name": {
                                "english": "Conductors, Insulators, Semiconductors",
                                "hindi": "चालक, विद्युतरोधी, अर्धचालक"
                            },
                            "description": {
                                "english": "Metals: ρ ∼ 10⁻² to 10⁻⁸ Ωm\nInsulators: ρ ∼ 10¹¹ to 10¹⁹ Ωm\nSemiconductors: ρ ∼ 10⁻⁵ to 10⁶ Ωm\nExamples: Si, Ge (elemental), GaAs (compound)",
                                "hindi": "धातु: ρ ∼ 10⁻² से 10⁻⁸ Ωm\nविद्युतरोधी: ρ ∼ 10¹¹ से 10¹⁹ Ωm\nअर्धचालक: ρ ∼ 10⁻⁵ से 10⁶ Ωm\nउदाहरण: Si, Ge (तात्विक), GaAs (यौगिक)"
                            }
                        },
                        {
                            "id": "concept14_1_2",
                            "display_name": {
                                "english": "Energy Band Theory",
                                "hindi": "ऊर्जा बैंड सिद्धांत"
                            },
                            "description": {
                                "english": "Valence band: Highest occupied band\nConduction band: Next allowed band\nBand gap E_g: Between valence and conduction\nMetals: E_g = 0 or overlapping\nInsulators: E_g > 3 eV\nSemiconductors: E_g < 3 eV",
                                "hindi": "संयोजकता बैंड: उच्चतम भरा बैंड\nचालन बैंड: अगला अनुमत बैंड\nबैंड अंतराल E_g: संयोजकता एवं चालन के मध्य\nधातु: E_g = 0 या अतिव्यापन\nविद्युतरोधी: E_g > 3 eV\nअर्धचालक: E_g < 3 eV"
                            }
                        }
                    ]
                },
                {
                    "id": "topic14_2",
                    "display_name": {
                        "english": "INTRINSIC AND EXTRINSIC SEMICONDUCTORS",
                        "hindi": "नैज एवं बाह्य अर्धचालक"
                    },
                    "article_range": "Sections 14.3-14.4",
                    "concepts": [
                        {
                            "id": "concept14_2_1",
                            "display_name": {
                                "english": "Intrinsic Semiconductor",
                                "hindi": "नैज अर्धचालक"
                            },
                            "description": {
                                "english": "Pure semiconductor\nn_e = n_h = n_i (intrinsic concentration)\nElectron-hole pairs created by thermal energy\nRecombination: e⁻ + hole → energy\nConduction by both electrons and holes",
                                "hindi": "शुद्ध अर्धचालक\nn_e = n_h = n_i (नैज सांद्रता)\nतापीय ऊर्जा से इलेक्ट्रॉन-होल युग्म बनते हैं\nपुनर्संयोजन: e⁻ + होल → ऊर्जा\nइलेक्ट्रॉन एवं होल दोनों से चालन"
                            }
                        },
                        {
                            "id": "concept14_2_2",
                            "display_name": {
                                "english": "n-type Semiconductor",
                                "hindi": "n-प्रकार अर्धचालक"
                            },
                            "description": {
                                "english": "Doped with pentavalent atoms (P, As, Sb)\nDonor impurities → extra electrons\nMajority carriers: electrons\nn_e >> n_h\nDonor energy level near conduction band",
                                "hindi": "पंचसंयोजी परमाणुओं से अपमिश्रित (P, As, Sb)\nदाता अशुद्धियाँ → अतिरिक्त इलेक्ट्रॉन\nबहुसंख्यक वाहक: इलेक्ट्रॉन\nn_e >> n_h\nदाता ऊर्जा स्तर चालन बैंड के पास"
                            }
                        },
                        {
                            "id": "concept14_2_3",
                            "display_name": {
                                "english": "p-type Semiconductor",
                                "hindi": "p-प्रकार अर्धचालक"
                            },
                            "description": {
                                "english": "Doped with trivalent atoms (B, Al, In)\nAcceptor impurities → holes\nMajority carriers: holes\nn_h >> n_e\nAcceptor level near valence band",
                                "hindi": "त्रिसंयोजी परमाणुओं से अपमिश्रित (B, Al, In)\nग्राही अशुद्धियाँ → होल\nबहुसंख्यक वाहक: होल\nn_h >> n_e\nग्राही स्तर संयोजकता बैंड के पास"
                            }
                        },
                        {
                            "id": "concept14_2_4",
                            "display_name": {
                                "english": "Mass Action Law",
                                "hindi": "द्रव्य अनुपाती क्रिया का नियम"
                            },
                            "description": {
                                "english": "n_e n_h = n_i²\nIn n-type: n_e ≈ N_D, n_h = n_i²/N_D\nIn p-type: n_h ≈ N_A, n_e = n_i²/N_A\nN_D, N_A = donor, acceptor concentrations",
                                "hindi": "n_e n_h = n_i²\nn-प्रकार में: n_e ≈ N_D, n_h = n_i²/N_D\np-प्रकार में: n_h ≈ N_A, n_e = n_i²/N_A\nN_D, N_A = दाता, ग्राही सांद्रताएँ"
                            }
                        }
                    ]
                },
                {
                    "id": "topic14_3",
                    "display_name": {
                        "english": "p-n JUNCTION DIODE",
                        "hindi": "p-n संधि डायोड"
                    },
                    "article_range": "Sections 14.5-14.6",
                    "concepts": [
                        {
                            "id": "concept14_3_1",
                            "display_name": {
                                "english": "Junction Formation",
                                "hindi": "संधि निर्माण"
                            },
                            "description": {
                                "english": "Diffusion: e⁻ (n→p), holes (p→n)\nDepletion region: Immobile ions\nBuilt-in potential V₀ (barrier)\nDrift current opposes diffusion\nAt equilibrium: No net current",
                                "hindi": "विसरण: e⁻ (n→p), होल (p→n)\nअवक्षय क्षेत्र: अगतिशील आयन\nअंतर्निहित विभव V₀ (बैरियर)\nअपवाह धारा विसरण का विरोध करती है\nसाम्यावस्था पर: कोई नेट धारा नहीं"
                            }
                        },
                        {
                            "id": "concept14_3_2",
                            "display_name": {
                                "english": "Forward Bias",
                                "hindi": "अग्र अभिनति"
                            },
                            "description": {
                                "english": "p to +ve, n to -ve\nBarrier height decreases\nDepletion width decreases\nMajority carrier injection\nLarge current (mA)\nV_th (Si ≈ 0.7V, Ge ≈ 0.3V)",
                                "hindi": "p धन से, n ऋण से जुड़ा\nबैरियर ऊँचाई घटती है\nअवक्षय चौड़ाई घटती है\nबहुसंख्यक वाहक अन्तःक्षेप\nअधिक धारा (mA)\nV_th (Si ≈ 0.7V, Ge ≈ 0.3V)"
                            }
                        },
                        {
                            "id": "concept14_3_3",
                            "display_name": {
                                "english": "Reverse Bias",
                                "hindi": "पश्च अभिनति"
                            },
                            "description": {
                                "english": "p to -ve, n to +ve\nBarrier height increases\nDepletion width increases\nMinority carrier drift\nSmall current (μA) - reverse saturation\nBreakdown at high V",
                                "hindi": "p ऋण से, n धन से जुड़ा\nबैरियर ऊँचाई बढ़ती है\nअवक्षय चौड़ाई बढ़ती है\nअल्पसंख्यक वाहक अपवाह\nअल्प धारा (μA) - पश्च संतृप्ति धारा\nउच्च V पर भंजन"
                            }
                        },
                        {
                            "id": "concept14_3_4",
                            "display_name": {
                                "english": "V-I Characteristics",
                                "hindi": "V-I अभिलक्षण"
                            },
                            "description": {
                                "english": "Forward: Exponential increase after knee voltage\nReverse: Very small constant current\nBreakdown: Sudden large current at V_br\nDynamic resistance r_d = ΔV/ΔI\nRectification: AC → DC",
                                "hindi": "अग्र: नी वोल्टता के बाद घातांकीय वृद्धि\nपश्च: बहुत कम स्थिर धारा\nभंजन: V_br पर अचानक अधिक धारा\nगतिक प्रतिरोध r_d = ΔV/ΔI\nदिष्टकारण: AC → DC"
                            }
                        }
                    ]
                },
                {
                    "id": "topic14_4",
                    "display_name": {
                        "english": "APPLICATIONS OF DIODE",
                        "hindi": "डायोड के अनुप्रयोग"
                    },
                    "article_range": "Section 14.7",
                    "concepts": [
                        {
                            "id": "concept14_4_1",
                            "display_name": {
                                "english": "Half Wave Rectifier",
                                "hindi": "अर्ध तरंग दिष्टकारी"
                            },
                            "description": {
                                "english": "Conducts only during one half cycle\nOutput: Pulsating DC\nFrequency = input frequency\nEfficiency: η = 40.6%\nRipple factor: γ = 1.21",
                                "hindi": "केवल एक अर्ध चक्र में चालन\nनिर्गत: स्पंदित DC\nआवृत्ति = निवेशी आवृत्ति\nदक्षता: η = 40.6%\nउर्मिका गुणांक: γ = 1.21"
                            }
                        },
                        {
                            "id": "concept14_4_2",
                            "display_name": {
                                "english": "Full Wave Rectifier",
                                "hindi": "पूर्ण तरंग दिष्टकारी"
                            },
                            "description": {
                                "english": "Conducts in both half cycles\nCentre-tap transformer or bridge rectifier\nOutput frequency = 2 × input frequency\nEfficiency: η = 81.2%\nRipple factor: γ = 0.48\nFilter (capacitor) smoothens output",
                                "hindi": "दोनों अर्ध चक्रों में चालन\nकेंद्र-टैप ट्रांसफॉर्मर या सेतु दिष्टकारी\nनिर्गत आवृत्ति = 2 × निवेशी आवृत्ति\nदक्षता: η = 81.2%\nउर्मिका गुणांक: γ = 0.48\nफिल्टर (संधारित्र) निर्गत को समतल करता है"
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
        "physics": 150,      # Changed from "chemistry" to "physics"
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
        "physics": "#FF9933",      # Changed from "chemistry" to "physics"
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
    format_func=lambda x: LANGUAGES[x], key= "phy"
)

st.sidebar.markdown("---")
st.sidebar.title("Instructions / निर्देश")
if selected_language == "english":
    st.sidebar.markdown("""
    - **Click** on PHYSICS to show/hide everything
    - **Double-click** on any CHAPTER to expand/collapse
    - **Double-click** on any TOPIC to expand/collapse
    - **Double-click** on any CONCEPT to show/hide details
    - **Double-click** on details to hide them
    """)
else:
    st.sidebar.markdown("""
    - **क्लिक करें** भौतिक विज्ञान पर सब कुछ दिखाने/छिपाने के लिए
    - **डबल-क्लिक करें** किसी भी अध्याय पर विस्तार/संक्षिप्त करने के लिए
    - **डबल-क्लिक करें** किसी भी विषय पर विस्तार/संक्षिप्त करने के लिए
    - **डबल-क्लिक करें** किसी भी अवधारणा पर विवरण दिखाने/छिपाने के लिए
    - **डबल-क्लिक करें** विवरण पर उसे छिपाने के लिए
    """)

st.title("Physics Mind Map / भौतिक विज्ञान माइंड मैप")
st.caption(f"Subject: Physics | विषय: भौतिक विज्ञान")

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
    physics_title = lang_config["title"]
    
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
const PHYSICS_TITLE = "{physics_title}";
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
        physics: true          // Changed from "chemistry" to "physics"
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
    
    const COLOR_PHYSICS = layoutConfig.colors.physics;      // Changed from COLOR_CHEMISTRY
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
        const maxWidth = n.type === "description" ? 480 : (n.type === "physics" ? 600 : 400);  // Changed from "chemistry"
        
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
        if (node.type === "physics") {{      // Changed from "chemistry"
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
        if (node.type === "physics") {{      // Changed from "chemistry"
            return states.physics;
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
        
        if(states.physics === true)  {{      // Changed from "chemistry"
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
        
        let physicsSize = calculateBoxSize(PHYSICS_TITLE, "physics");    // Changed from "chemistry"
        let physicsY = states.physics ? canvas.height/2 : 150;           // Changed from "chemistry"
        
        nodes.physics = {{                                                 // Changed from "chemistry"
            x: COLUMN_X.physics,                                          // Changed from COLUMN_X.chemistry
            y: physicsY,
            width: physicsSize.width,
            height: physicsSize.height,
            text: PHYSICS_TITLE,
            color: COLOR_PHYSICS,                                         // Changed from COLOR_CHEMISTRY
            type: "physics"                                               // Changed from "chemistry"
        }};

        canvas.width = 2500;
    }}

    // Draw everything
    function draw() {{
        ctx.clearRect(0, 0, canvas.width, canvas.height);
        ctx.beginPath();
       
        calculateLayout();

        if(states.physics === true) {{      // Changed from "chemistry"
            // Draw connections
            chaptersConfig.forEach(chapter => {{
                if(nodes[chapter.id]) drawCurvedConnection(nodes.physics, nodes[chapter.id]);   // Changed from nodes.chemistry
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
        
        if(nodes.physics && inside(mx, my, nodes.physics)) {{      // Changed from nodes.chemistry
            states.physics = !states.physics;                      // Changed from states.chemistry
            
            if(!states.physics) {{                                 // Changed from states.chemistry
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
        
        if(!states.physics) return;    // Changed from states.chemistry
    }});

    canvas.addEventListener("dblclick", e => {{
        const rect = canvas.getBoundingClientRect();
        const scaleX = canvas.width / rect.width;
        const scaleY = canvas.height / rect.height;
        
        const mx = (e.clientX - rect.left) * scaleX;
        const my = (e.clientY - rect.top) * scaleY;
        
        let found = false;
        
        if(!states.physics) return;    // Changed from states.chemistry
        
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
html_content = generate_bilingual_html(PHYSICS_CONFIG, LAYOUT_CONFIG, selected_language)
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
        **Physics Mind Map** - Complete Class 12 Physics
        
        **Chapter 1:** Electric Charges and Fields
        **Chapter 2:** Electrostatic Potential and Capacitance
        **Chapter 3:** Current Electricity
        **Chapter 4:** Moving Charges and Magnetism
        **Chapter 5:** Magnetism and Matter
        **Chapter 6:** Electromagnetic Induction
        **Chapter 7:** Alternating Current
        **Chapter 8:** Electromagnetic Waves
        
        Complete with formulas, examples and key concepts
        """)
    else:
        st.markdown("""
        **भौतिक विज्ञान माइंड मैप** - संपूर्ण कक्षा 12 भौतिकी
        
        **अध्याय 1:** वैद्युत आवेश तथा क्षेत्र
        **अध्याय 2:** स्थिरवैद्युत विभव एवं धारिता
        **अध्याय 3:** विद्युत धारा
        **अध्याय 4:** गतिमान आवेश और चुंबकत्व
        **अध्याय 5:** चुंबकत्व एवं द्रव्य
        **अध्याय 6:** वैद्युतचुंबकीय प्रेरण
        **अध्याय 7:** प्रत्यावर्ती धारा
        **अध्याय 8:** वैद्युतचुंबकीय तरंगें
        
        सूत्रों, उदाहरणों और मुख्य अवधारणाओं सहित
        """)

with col2:
    st.markdown("### 🎯 How to Use")
    if selected_language == "english":
        st.markdown("""
        1. **Click** PHYSICS to show/hide all
        2. **Double-click** any CHAPTER to expand
        3. **Double-click** any TOPIC to expand
        4. **Double-click** any CONCEPT for details
        5. **Double-click** details to hide
        """)
    else:
        st.markdown("""
        1. **क्लिक करें** भौतिक विज्ञान पर सब दिखाने/छिपाने के लिए
        2. **डबल-क्लिक करें** किसी भी अध्याय पर विस्तार करने के लिए
        3. **डबल-क्लिक करें** किसी भी विषय पर विस्तार करने के लिए
        4. **डबल-क्लिक करें** किसी भी अवधारणा पर विवरण के लिए
        5. **डबल-क्लिक करें** विवरण पर छिपाने के लिए
        """)

with col3:
    st.markdown("### 📊 Content")
    if selected_language == "english":
        st.markdown("""
        **Physics Content:**
        - Chapters: 8
        - Topics: 20+
        - Concepts: 50+
        - Key Formulas: 100+
        - Bilingual: English/Hindi
        """)
    else:
        st.markdown("""
        **भौतिक विज्ञान सामग्री:**
        - अध्याय: 8
        - विषय: 20+
        - अवधारणाएं: 50+
        - मुख्य सूत्र: 100+
        - द्विभाषी: अंग्रेजी/हिंदी
        """)

# Debug
if st.checkbox("Show Debug Info / डीबग जानकारी दिखाएं", key="phy_debug"):
    total_chapters = len(PHYSICS_CONFIG["chapters"])
    total_topics = 0
    total_concepts = 0
    for chapter in PHYSICS_CONFIG["chapters"]:
        total_topics += len(chapter["topics"])
        for topic in chapter["topics"]:
            total_concepts += len(topic["concepts"])
    
    st.json({
        "main_title": "PHYSICS",
        "total_chapters": total_chapters,
        "total_topics": total_topics,
        "total_concepts": total_concepts,
        "current_language": selected_language
    })
