from typing import Dict, List


class SambalpuriGrammar:

    def __init__(self):
        self.verb_conjugation = self._load_verb_conjugation()
        self.negation = self._load_negation()
        self.nominal_morphology = self._load_nominal_morphology()
        self.pronoun_paradigms = self._load_pronoun_paradigms()
        self.syntax = self._load_syntax()

    def _load_verb_conjugation(self) -> Dict:
        """
        Sambalpuri verbs are partially agglutinating and partially inflectional
        (Behera et al. 2021: 58; Mohapatra & Hembram 2010: 206-7).
        Verbs inflect for tense (present, past, future), aspect
        (progressive, perfect, perfect progressive), person, number,
        and honorificity. In negative constructions, person/number
        agreement is often lost (Kushal 2023: 115-116).
        """

        kha_paradigm = {
            "infinitive": "kʰɑ",
            "meaning": "to eat",

            "present_simple": {
                "description": (
                    "Tense marker -ɛs- present in affirmative. "
                    "Lost in negative. Person/number retained in both."
                ),
                "affirmative": {
                    "1sg": "kʰɑɛsĩ",
                    "1pl": "kʰɑɛsũ",
                    "2sg": "kʰɑɛsu",
                    "2pl": "kʰɑɛsə",
                    "3sg": "kʰɑɛsi",
                    "3pl": "kʰɑɛsən"
                },
                "negative": {
                    "1sg": "ne kʰẽ",
                    "1pl": "ne kʰəũ",
                    "2sg": "ne kʰəu",
                    "2pl": "ne kʰə",
                    "3sg": "ne kʰe",
                    "3pl": "ne kʰɑ:n"
                }
            },

            "present_progressive": {
                "description": (
                    "Formed with -u- progressive marker + auxiliary cʰe. "
                    "In negative, verb shifts to infinitival form; "
                    "person/number agreement lost across all persons."
                ),
                "affirmative": {
                    "1sg": "kʰəucʰẽ",
                    "1pl": "kʰəucʰũ",
                    "2sg": "kʰəucʰu",
                    "2pl": "kʰəucʰə",
                    "3sg": "kʰəucʰe",
                    "3pl": "kʰəucʰən"
                },
                "negative": {
                    "all_persons": "ne kʰɑɛbɑr",
                    "note": (
                        "Uniform across all persons/numbers — "
                        "agreement fully neutralised in negative."
                    )
                }
            },

            "present_perfect": {
                "description": (
                    "Formed with -i- perfective marker + auxiliary cʰe. "
                    "Negative uses uniform form; agreement neutralised."
                ),
                "affirmative": {
                    "1sg": "kʰɑicʰẽ",
                    "1pl": "kʰɑicʰũ",
                    "2sg": "kʰɑicʰu",
                    "2pl": "kʰɑicʰə",
                    "3sg": "kʰɑicʰe",
                    "3pl": "kʰɑicʰən"
                },
                "negative": {
                    "all_persons": "ne kʰei",
                    "note": "Uniform across all persons/numbers."
                }
            },

            "past_simple": {
                "description": (
                    "Tense marker present in affirmative. "
                    "Lost in negative. "
                    "Agreement neutralised in negative, "
                    "yielding a form identical in appearance "
                    "to present perfect negative (Kushal 2023: 119)."
                ),
                "affirmative": {
                    "1sg": "kʰɑɛli",
                    "1pl": "kʰɑɛlu",
                    "2sg": "kʰɑɛlu",
                    "2pl": "kʰɑɛlə",
                    "3sg": "kʰɑɛlɑ",
                    "3pl": "kʰɑɛle"
                },
                "negative": {
                    "all_persons": "ne kʰei",
                    "note": (
                        "Uniform across all persons/numbers. "
                        "Tense marker lost."
                    )
                }
            },

            "past_progressive": {
                "description": (
                    "Formed with -u- + past auxiliary t̪ʰilɑ. "
                    "Negative retains progressive marker "
                    "but neutralises agreement."
                ),
                "affirmative": {
                    "1sg": "kʰəut̪ʰili",
                    "1pl": "kʰəut̪ʰilu",
                    "2sg": "kʰəut̪ʰilu",
                    "2pl": "kʰəut̪ʰilə",
                    "3sg": "kʰəut̪ʰilɑ",
                    "3pl": "kʰəut̪ʰile"
                },
                "negative": {
                    "all_persons": "ne kʰəut̪ʰei",
                    "note": "Progressive marker retained; agreement neutralised."
                }
            },

            "future_simple": {
                "description": (
                    "Future uses distinct suffixes (-mi, -mu, -bu etc.). "
                    "Crucially, unlike present/past, person/number "
                    "agreement is RETAINED in future negatives "
                    "(Kushal 2023: 121). Tense marker lost."
                ),
                "affirmative": {
                    "1sg": "kʰɑɛmi",
                    "1pl": "kʰɑɛmu",
                    "2sg": "kʰɑɛbu",
                    "2pl": "kʰɑɛbə",
                    "3sg": "kʰɑɛbɑ",
                    "3pl": "kʰɑɛbe"
                },
                "negative": {
                    "1sg": "ne kʰẽ",
                    "1pl": "ne kʰəũ",
                    "2sg": "ne kʰəu",
                    "2pl": "ne kʰə",
                    "3sg": "ne kʰe",
                    "3pl": "ne kʰɑ:n"
                }
            },

            "future_progressive": {
                "description": (
                    "Agreement retained in negative, unlike present/past progressive."
                ),
                "affirmative": {
                    "1sg": "kʰəut̪ʰimi",
                    "1pl": "kʰəut̪ʰimu",
                    "2sg": "kʰəut̪ʰibu",
                    "2pl": "kʰəut̪ʰibə",
                    "3sg": "kʰəut̪ʰibɑ",
                    "3pl": "kʰəut̪ʰibe"
                },
                "negative": {
                    "1sg": "ne kʰəut̪ʰẽ",
                    "1pl": "ne kʰəut̪ʰəu",
                    "2sg": "ne kʰəut̪ʰəu",
                    "2pl": "ne kʰəut̪ʰə",
                    "3sg": "ne kʰəut̪ʰe",
                    "3pl": "ne kʰəut̪ʰɑn"
                }
            }
        }

        other_verbs = {
            "jɑ/pōvuni_equiv": {
                "infinitive": "jɑ-",
                "meaning": "to go",
                "example_prs_3sg_aff": "jɑicʰe",
                "example_prs_3sg_neg": "ne jeĩ",
                "example_pst_3sg_aff": "ɡəlɑ",
                "example_pst_3sg_neg": "ne jeĩ"
            },
            "nɑc-": {
                "infinitive": "nɑc-",
                "meaning": "to dance",
                "example_prs_prog_aff": "nɑcucʰe (3SG)",
                "example_prs_prog_neg": "ne nɑcbɑr (all persons)"
            },
            "kər-": {
                "infinitive": "kər-",
                "meaning": "to do",
                "example_prs_1sg_aff": "kərsi",
                "example_prs_1sg_neg": "ne kərẽ"
            },
            "bɑr-/barpuni_equiv": {
                "infinitive": "bɑr-",
                "meaning": "to come",
                "example_pst_3sg_aff": "ɑsbɑ (will come, FUT)",
                "example_pst_3sg_neg": "ne ɑse"
            },
            "sun-": {
                "infinitive": "sun-",
                "meaning": "to listen",
                "imperative_aff": "sun",
                "imperative_neg": "ne sun"
            },
            "kʰɛl-": {
                "infinitive": "kʰɛl-",
                "meaning": "to play",
                "example_prs_1sg_aff": "kʰɛlsi",
                "example_prs_1sg_neg": "ne kʰɛlẽ"
            },
            "rɑnd̪ʰ-": {
                "infinitive": "rɑnd̪ʰ-",
                "meaning": "to cook",
                "example_prf_neg": "ne rɑnd̪ʰi"
            },
            "pəḍʰ-": {
                "infinitive": "pəḍʰ-",
                "meaning": "to study/read",
                "example_fut_3sg_aff": "pəḍʰbɑ",
                "example_fut_3sg_neg": "ne pəḍʰe"
            },
            "d̪ɛkʰ-": {
                "infinitive": "d̪ɛkʰ-",
                "meaning": "to see",
                "example_pst_1sg_aff": "d̪ɛkʰlĩ",
                "example_pst_1sg_neg": "ne d̪ɛkʰi"
            },
            "nərd̪-": {
                "infinitive": "nərd̪ɪba",
                "meaning": "to run (Bolangiri variety)",
                "note": "Cf. d̪əud̺ɪba in standard Sambalpuri"
            }
        }

        return {
            "verbs": {"kʰɑ (paradigm verb)": kha_paradigm, **other_verbs},
            "total_paradigm_verb": "kʰɑ- (to eat)",
            "morphophonological_patterns": [
                "Tense marker -ɛs- present in simple present affirmative; lost in negative",
                "Progressive marker -u- retained even in negative constructions",
                "Perfective marker -i- retained in negative constructions",
                "Past auxiliary: t̪ʰilɑ (affirmative) → t̪ʰei (negative) in progressive/perfect",
                (
                    "Person/number agreement LOST in negative: present progressive, "
                    "present perfect, past simple, past progressive, past perfect"
                ),
                (
                    "Person/number agreement RETAINED in negative: "
                    "present simple, future (all forms)"
                ),
                "Asymmetric negation (A/Cat type, Miestamo 2005) is the dominant pattern",
                "Honorific verbal forms: root (informal) → +HON suffix (formal) → +HON+un (extra polite)"
            ]
        }

    def _load_negation(self) -> Dict:
        """
        Based on Kushal (2023). Sambalpuri has three distinct negative
        particles distributed across syntactic environments.
        The standard negator has four dialectal variants used
        interchangeably without semantic difference.
        """
        return {
            "negative_particles": {
                "standard_negator": {
                    "forms": ["ne", "nei", "nɑi", "ni"],
                    "distribution": (
                        "Used in all clausal/verbal negation contexts: "
                        "declaratives, imperatives, questions, "
                        "subordinate clauses, coordination, conditionals"
                    ),
                    "position": "Preverbal (always precedes the verb it negates)",
                    "dialectal_note": (
                        "ne/nei dominant in Sambalpur district; "
                        "ni in Bolangiri/Sundargarhi; "
                        "nuhe/nihe in Bargarh district (Patel 2000)"
                    )
                },
                "non_verbal_negator": {
                    "forms": ["nuhe", "nuhese"],
                    "distribution": (
                        "Used exclusively in non-verbal clauses "
                        "of equation, proper inclusion, and attribution types. "
                        "Example: se mor mɑ nuhese (She is not my mother)"
                    ),
                    "position": "Post-predicate (fused with copula)"
                },
                "abessive_negator": {
                    "forms": ["bin", "binɑ"],
                    "meaning": "without",
                    "distribution": (
                        "Used only in conjunctive participle (converb) constructions. "
                        "Example: muĩ ɡurəs binɑ pi kəri suili "
                        "(I slept without drinking milk). "
                        "Preferred by native speakers over standard negator "
                        "in this construction."
                    )
                }
            },

            "clausal_negation": {
                "standard_negation": {
                    "description": (
                        "Negates declarative verbal main clauses. "
                        "Negator placed preverbally. "
                        "Results in asymmetric paradigm (A/Cat type): "
                        "verbal structure changes, tense marker often lost."
                    ),
                    "examples": [
                        {
                            "affirmative": "ṭukel-ṭɑ nɑc-u-cʰe (The girl is dancing)",
                            "negative": "ṭukel-ṭɑ ne nɑcbɑr (The girl is not dancing)"
                        },
                        {
                            "affirmative": "muĩ bʰɑt̪ kʰɑɛsi (I eat rice)",
                            "negative": "muĩ bʰɑt̪ ne kʰẽ (I do not eat rice)"
                        }
                    ]
                },
                "imperative_negation": {
                    "description": (
                        "Type 1 prohibitive (van der Auwera & Lejeune 2013): "
                        "same structure as positive imperative, same negator. "
                        "Symmetric construction. Honorific distinctions preserved."
                    ),
                    "informal": "ne kʰɑ (Don't eat)",
                    "formal": "ne kʰə (Don't eat — honorific)",
                    "extra_polite": "ne kʰəun (Don't eat — highly respectful)"
                },
                "question_negation": {
                    "description": (
                        "Yes/no questions use obligatory question morpheme kɛ̃ "
                        "at sentence end. Negator remains preverbal. "
                        "Wh-questions use same negator without question morpheme."
                    ),
                    "yes_no_example": "t̪ui ɑm ne kʰəu kɛ̃? (Don't you eat mango?)",
                    "wh_example": "kie ne kʰei (Who has not eaten?)"
                },
                "non_verbal_clause_negation": {
                    "equation": "se mor mɑ nuhe/nuhese (She is not my mother)",
                    "proper_inclusion": "kukur pəsu-ṭe nuhe/nuhese (Dog is not an animal)",
                    "attribution": "se kɑɳɑ nuhe/nuhese (He is not blind)",
                    "locative": "bilei-ṭɑ kʰəṭ t̪əle ne nə (The cat is not under the cot)",
                    "existential": "jəŋɡle bɑɡʰ ne nə (There is no tiger in the forest)",
                    "possessive": "mɑnəsi-r kɑr ne nə (Manasi has no car)",
                    "note": (
                        "First three types (equation, inclusion, attribution) use nuhe/nuhese; "
                        "last three (locative, existential, possessive) use ne + obligatory copula nə"
                    )
                },
                "non_main_clause_negation": {
                    "finite_subordinate": (
                        "Same negator ne used. "
                        "Example: mor biswɑs je se ne ɑse "
                        "(I believe that he will not come)"
                    ),
                    "non_finite_subordinate": (
                        "Non-finite clauses CANNOT be negated in Sambalpuri. "
                        "muĩ t̪ɑr ne ɑɛbɑr d̪ɛkʰlĩ is ungrammatical "
                        "(Kushal 2023: 130)"
                    )
                }
            },

            "non_clausal_negation": {
                "negative_replies": (
                    "Both one-word reply (nei) and verb repetition possible. "
                    "Example: kukur-ṭɑ bʰukucʰe kɛ̃? → nei / nei, ne bʰukbɑr"
                ),
                "negative_indefinite_pronouns": {
                    "description": (
                        "No inherent negative indefinite pronouns. "
                        "Indefinite pronouns obligatorily co-occur with clausal negator. "
                        "Omission of negator renders sentence ungrammatical."
                    ),
                    "examples": [
                        "kihe ne ɑsi (Nobody came)",
                        "se kicʰi ne neĩ (He has taken nothing)",
                        "se kɑhɑkũ ne bʰɛṭlɑ (He met nobody)"
                    ],
                    "note": (
                        "kicʰi (something/anything) is polarity-neutral: "
                        "used in both affirmative and negative. "
                        "kie (someone) → kihe (nobody) when verb is negated."
                    )
                },
                "negative_quantifiers": (
                    "No dedicated negative quantifiers. "
                    "Standard negation obligatorily added."
                )
            },

            "scope_of_negation": {
                "description": (
                    "Negator always precedes the constituent it scopes over. "
                    "Can be moved to negate different parts of the sentence. "
                    "When sentence-initial (nei), interpreted as propositional negation. "
                    "Intonation/stress can shift scope without moving the negator."
                ),
                "examples": [
                    {
                        "sentence": (
                            "mɑnəsi əu mɑnəs kət̪ʰɑ həut̪ʰile ne pəḍʰut̪ʰei"
                        ),
                        "gloss": "Manasi and Manas were talking, (but) not studying"
                    },
                    {
                        "sentence": (
                            "mɑnəsi əu mɑnəs ne kət̪ʰɑ həut̪ʰei pəḍʰut̪ʰile"
                        ),
                        "gloss": "Manasi and Manas were not talking, (but they were) studying"
                    }
                ]
            },

            "negative_polarity_items": {
                "description": (
                    "NPIs formed with indefinite pronoun + particle bi/bʰi: (even/also). "
                    "Grammatical only within scope of negation."
                ),
                "examples": [
                    "kihe bi: bhuji kʰɑi ne ɑsle (Nobody came to attend the feast)",
                    "jənɛ bi iskul-ke ne ɑsi (Not even one has come to school)",
                    "se kɛbʰe ne pədʰe (He never studies)"
                ]
            },

            "double_negation": (
                "Not permitted. "
                "Only a single negator per clause is grammatical. "
                "muĩ ne kicʰi ne d̪ɛkʰi is ungrammatical (Kushal 2023: 137)."
            ),

            "negation_in_coordination": (
                "Standard negator used preverbally in each coordinated clause. "
                "No special negative coordinator (unlike English neither...nor). "
                "Example: muĩ ne pəḍʰẽ əu iskul-ke ne jẽ "
                "(I will not study and will not go to school either)"
            ),

            "negation_in_conditionals": (
                "Same negator in both if-clause and matrix clause, preverbal. "
                "Example: se ne ḍɑk-le mui ne jẽ "
                "(If he does not invite, I will not go)"
            )
        }

    def _load_nominal_morphology(self) -> Dict:
        """
        Sambalpuri nominal morphology shows agglutinating features.
        Suffixes, postpositions, and case endings agglutinate with nouns
        (Behera et al. 2021: 58, citing Mohapatra & Hembram 2010).
        Multiple suffixes can stack on a single base (case stacking).
        """
        return {
            "agglutination": {
                "description": (
                    "Nominal morphology is predominantly agglutinating; "
                    "verbal morphology shows inflectional features. "
                    "A language can be both simultaneously "
                    "(Haspelmath 2009; Greenberg 1954 [1960]: 182)."
                ),
                "case_stacking_example": {
                    "sambalpuri": "ma:s̪tar-ma:n-kar-nu",
                    "gloss": "teacher + PLURAL + HON.GEN + LOCATIVE/ABLATIVE",
                    "translation": "from the teachers",
                    "odia_equivalent": "fikʲjɔkɔ-ma:n-ɔnkɔ-tʰɑ:ru"
                }
            },

            "pluralisation": {
                "human_plural": "-ma:n (honorific plural marker for humans)",
                "non_human_plural": "contextually marked",
                "example": "ma:s̪tar-ma:n (teachers)"
            },

            "classifiers": {
                "description": (
                    "Numeral classifiers attach to numerals. "
                    "Human countable: -j̪ʰun (Sambalpuri) vs -jɔnɔ (Odia). "
                    "Non-human countable: -ta: (Sambalpuri) vs -ti (Odia)."
                ),
                "examples": [
                    "ca:r-jʰun lok (four-CLF men) [Sambalpuri]",
                    "cha:ri-janɔ lokɔ (four-CLF men) [Odia]",
                    "ca:r-ta gacʰ (four-CLF trees) [Sambalpuri]",
                    "ca:r-ti gɔcʰɔ (four-CLF trees) [Odia]"
                ]
            },

            "postpositions": {
                "description": (
                    "Sambalpuri uses postpositions (head-final, "
                    "consistent with SOV order)."
                ),
                "sambalpuri_postpositions": {
                    "lekʰe": "like/similar to",
                    "a:gru": "before/in front of",
                    "saŋe": "with/together",
                    "a:gaṭu": "in front of",
                    "ṭak": "up to/until"
                },
                "odia_equivalents": {
                    "bʰɔli": "like",
                    "purbaru": "before",
                    "sɔhɔ": "with",
                    "a:goa:ṭu": "in front of",
                    "pɔrjɔntɔ": "up to"
                },
                "example": (
                    "mui ta:r lekʰe sa:t-te pindʲicʰe "
                    "(I have worn shirt like him)"
                )
            },

            "honorifics": {
                "description": (
                    "Honorific distinctions marked morphologically "
                    "on both nominals and verbs. "
                    "-ma:n marks honorific human plural; "
                    "genitive -kar- used with honorific plural "
                    "(vs plain genitive -r-)."
                ),
                "example": {
                    "hon_gen": "ma:s̪tar-ma:n-kar (of the teachers, HON)",
                    "plain_gen": "aval-r (her/his, plain)"
                }
            },

            "emphatic_particles": {
                "bi_bʰi:": "even/also — used in NPI constructions with negation",
                "example": "kihe bi: ne ɑsi (Nobody came, lit. whoever even NEG came)"
            },

            "spatio_temporal_nouns": {
                "now_standard": "iʰade",
                "now_sundargarh": "ɛkʰɛn",
                "now_subarnapur": "iɡʰɔdi",
                "note": "Dialectal variation documented by Patel (2000)"
            }
        }

    def _load_pronoun_paradigms(self) -> Dict:
        """
        Personal pronouns from Kushal (2023) glossing data.
        Sambalpuri distinguishes 1SG/1PL, 2SG/2PL, and 3SG/3PL.
        No explicit inclusive/exclusive first plural distinction
        documented in the current sources (contrast Tulu).
        Dative case marked by postposition -ke/-ke after pronoun.
        """
        return {
            "first_person": {
                "sg": {
                    "nom": "muĩ",
                    "gen": "mor",
                    "dat": "muĩ-ke (inferred)",
                    "note": "mor biswɑs = my belief (GEN)"
                },
                "pl": {
                    "nom": "ɑmẽ / ɑme",
                    "gen": "ɑmɑ- (inferred)",
                    "note": "ɑmẽ ne sun-u (We don't listen)"
                }
            },
            "second_person": {
                "sg": {
                    "nom": "t̪uĩ / t̪ui",
                    "dat": "t̪ɑr / t̪ɑt̪e / t̪ɑke (addressee DAT, HON)",
                    "note": "t̪uĩ bʰɑt̪ ne kʰəu (You do not eat rice)"
                }
            },
            "third_person": {
                "sg": {
                    "nom_masc_neut": "se",
                    "nom_fem": "se (no overt gender distinction in nominative)",
                    "gen": "t̪ɑr",
                    "dat": "t̪ɑr / t̪ɑt̪e / t̪ɑke",
                    "note": "se bʰɑt̪ ne kʰei (He has not eaten rice)"
                },
                "pl": {
                    "note": "Not explicitly paradigmed in current sources"
                }
            },
            "interrogative_pronouns": {
                "who": "kie (positive) / kihe (with negation = nobody)",
                "what_thing": "kicʰi (polarity-neutral: something/anything)",
                "whom": "kɑhɑkũ (somebody/nobody with negation)",
                "why": "kɑɛ̃",
                "question_morpheme": "kɛ̃ (sentence-final, marks yes/no questions)"
            }
        }

    def _load_syntax(self) -> Dict:
        """
        Sambalpuri is a canonical SOV language (Kushal 2023: 109;
        Behera et al. 2021: 52). It shares core typological features
        with other Indo-Aryan languages while showing influence from
        both Indo-Aryan (Chattisgarhi, Bagheli, Bhojpuri) and
        Dravidian contact (Behera et al. 2021: 53).
        """
        return {
            "word_order": "SOV",
            "example": (
                "muĩ bʰɑt̪ kʰɑɛsi "
                "(I rice eat) = 'I eat rice'"
            ),
            "postpositions": True,
            "example_postposition": (
                "jəŋɡle (forest-LOC), kʰəṭ t̪əle (cot under), "
                "ɡʰər-ke (home-LOC/DAT)"
            ),
            "negative_position": (
                "Preverbal in all tenses and moods. "
                "Negator always immediately precedes the verb it scopes over. "
                "Scope is moveable — constituent negation achieved by "
                "repositioning negator before target constituent."
            ),
            "subordination": {
                "complementiser": "je (that) — overt or covert",
                "example": (
                    "mor biswɑs je se ne ɑse "
                    "(I believe that he will not come)"
                )
            },
            "conditional": {
                "correlative_marker": "-le (if-suffix on verb)",
                "particle": "jədi (if)",
                "example": (
                    "se ne ḍɑk-le mui ne jẽ "
                    "(If he does not invite, I will not go)"
                )
            },
            "conjunctive_participle": {
                "description": (
                    "Converb construction: action completed before main verb. "
                    "Marked with kəri (CP marker). "
                    "Negated preferably with bin/binɑ (without) rather than ne."
                ),
                "example": (
                    "muĩ ɡurəs binɑ pi kəri suili "
                    "(I slept without drinking milk)"
                )
            },
            "coordination": {
                "coordinator": "əu (and)",
                "example": (
                    "mɑnəsi əu mɑnəs (Manasi and Manas)"
                )
            },
            "typological_classification": (
                "Indo-Aryan, SOV typology. "
                "Partially agglutinating (nominal) + partially inflectional (verbal). "
                "Described as unscheduled language, spoken in western Odisha "
                "across 11 districts (Kushal 2023: 110). "
                "Also known as Kosli/Koshali. "
                "Written using Odia script."
            ),
            "lexical_similarity_to_odia": (
                "52.46% (Behera & Dash 2017). "
                "Fully distinct vocabulary documented in many domains "
                "(see Table 1, Behera et al. 2021: 56)."
            )
        }

    def get_all_grammar(self) -> Dict:
        return {
            "verb_conjugation": self.verb_conjugation,
            "negation": self.negation,
            "nominal_morphology": self.nominal_morphology,
            "pronoun_paradigms": self.pronoun_paradigms,
            "syntax": self.syntax
        }

    def format_for_prompt(self) -> str:
        parts = []

        parts.append("**Verb Conjugation Rules:**")
        parts.append(
            "Sambalpuri verbs conjugate for tense, aspect, person, "
            "number, and honorificity. The paradigm verb is kʰɑ- (to eat). "
            "Key patterns:\n"
        )
        parts.append("Present simple (affirmative → negative):")
        parts.append("1sg: kʰɑɛsĩ → ne kʰẽ")
        parts.append("1pl: kʰɑɛsũ → ne kʰəũ")
        parts.append("2sg: kʰɑɛsu → ne kʰəu")
        parts.append("2pl: kʰɑɛsə → ne kʰə")
        parts.append("3sg: kʰɑɛsi → ne kʰe")
        parts.append("3pl: kʰɑɛsən → ne kʰɑ:n")
        parts.append(
            "Note: tense marker -ɛs- lost in negative; "
            "person/number retained in simple present and ALL future forms."
        )
        parts.append(
            "\nPresent progressive: kʰəucʰe (all persons) → "
            "ne kʰɑɛbɑr (uniform, agreement neutralised)"
        )
        parts.append(
            "Present perfect: kʰɑicʰe (all persons) → "
            "ne kʰei (uniform, agreement neutralised)"
        )
        parts.append(
            "Past simple: kʰɑɛlɑ (3SG) → ne kʰei (uniform)")
        parts.append(
            "Past progressive: kʰəut̪ʰilɑ (3SG) → ne kʰəut̪ʰei (uniform)"
        )
        parts.append(
            "Future simple: kʰɑɛbɑ (3SG) → ne kʰe (3SG) — "
            "agreement retained unlike past/present progressive\n"
        )

        parts.append("**Negation System:**")
        parts.append("Three negative particles:")
        parts.append(
            "1. ne/nei/nɑi/ni — standard negator (preverbal, all verbal clauses)"
        )
        parts.append(
            "2. nuhe/nuhese — non-verbal negator "
            "(equation/inclusion/attribution clauses)"
        )
        parts.append(
            "3. bin/binɑ — abessive (without), used in converb constructions\n"
        )
        parts.append("Negation position: always preverbal")
        parts.append("Negation type: asymmetric (A/Cat, Miestamo 2005)")
        parts.append(
            "Double negation: not permitted — one negator per clause only\n"
        )

        parts.append("**Nominal Morphology:**")
        parts.append(
            "Agglutinating: suffixes stack transparently on noun stems"
        )
        parts.append(
            "Classifiers: -jʰun (human), -ta: (non-human) "
            "attach to numerals"
        )
        parts.append(
            "Honorific plural: -ma:n (e.g. ma:s̪tar-ma:n = teachers)"
        )
        parts.append(
            "Case stacking: ma:s̪tar-ma:n-kar-nu "
            "(teacher+PL+HON.GEN+LOC/ABL = 'from the teachers')\n"
        )

        parts.append("**Pronoun System (attested forms):**")
        parts.append("1SG muĩ (NOM), mor (GEN)")
        parts.append("1PL ɑmẽ (NOM)")
        parts.append("2SG t̪uĩ (NOM), t̪ɑt̪e/t̪ɑke (DAT/HON)")
        parts.append("3SG se (NOM), t̪ɑr (GEN/DAT)")
        parts.append("Q-pronoun: kie (who) → kihe (nobody, with negation)")
        parts.append("Q-morpheme: kɛ̃ (sentence-final yes/no marker)\n")

        parts.append("**Syntax:**")
        parts.append(
            "- SOV word order: muĩ bʰɑt̪ kʰɑɛsi (I rice eat) = 'I eat rice'"
        )
        parts.append("- Postpositions: ɡʰər-ke (home-LOC), jəŋɡle (forest-LOC)")
        parts.append("- Complementiser: je (that) — may be covert")
        parts.append("- Conditional suffix: -le on verb (if-clause)")
        parts.append(
            "- Converb marker: kəri (CP); negated by bin/binɑ (without)"
        )
        parts.append(
            "- Scope of negation: negator precedes targeted constituent; "
            "moveable for focus"
        )

        return "\n".join(parts)