# Predefined concepts sets

Those concept sets can be found in `eds_scikit.datasets.default_concepts_sets`.

!!! question "How were the code selected ?"
      Each concept set codes were selected by coding system expert and validated through statistical analysis. However new codes may appear or become outdated. Feel free to propose new concept sets or concept codes !

=== "Blood Count Cell"

    | concepts_set_name                         | GLIMS_ANABIO_concept_code                                                |
    |:------------------------------------------|:-------------------------------------------------------------------------|
    | Hemoglobin_Blood_Count                    | ['A0163', 'H6738']                                                       |
    | Leukocytes_Blood_Count                    | ['A0174', 'H6740', 'C8824']                                              |
    | Platelets_Blood_Count                     | ['A0230', 'H6751', 'A1598', 'A1598', 'A2538', 'A2539', 'A2539', 'J4463'] |
    | Lymphocytes_Blood_Count                   | ['A0198', 'H6743']                                                       |
    | Monocytes_Blood_Count                     | ['A0210', 'H6747']                                                       |
    | Neutrophil_Polymorphonuclears_Blood_Count | ['A0155', 'H6732']                                                       |
    | Eosinophil_Polymorphonuclears_Blood_Count | ['A0150', 'H6730']                                                       |

=== "Ionogram"

    | concepts_set_name               | GLIMS_ANABIO_concept_code                                                         |
    |:--------------------------------|:----------------------------------------------------------------------------------|
    | Bicarbonate_Blood_Concentration | ['A0422', 'H9622', 'C6408', 'F4161', 'A2136', 'J7371', 'G2031']                   |
    | Calcium_Blood_Concentration     | ['C0543', 'D2359', 'A0038', 'H5041', 'F2625', 'L5047', 'A2512', 'A2512', 'A0607'] |
    | Chloride_Blood_Concentration    | ['A0079', 'J1179', 'F2619']                                                       |
    | Potassium_Blood_Concentration   | ['A2380', 'E2073', 'F2618', 'E2337', 'J1178']                                     |
    | Sodium_Blood_Concentration      | ['A0262', 'J1177', 'F8162', 'F2617']                                              |

=== "Blood Gas"

    | concepts_set_name               | GLIMS_ANABIO_concept_code   |
    |:--------------------------------|:----------------------------|
    | HCO3-_Blood_Concentration       | ['A0420', 'L5018']          |
    | Lactate_Gaz_Blood_Concentration | ['C8697', 'H7748']          |
    | PaCO2_Blood_Concentration       | ['A7305', 'A0630']          |
    | PaO2_Blood_Concentration        | ['A7319', 'H7747']          |
    | SaO2_Blood_Concentration        | ['A7334', 'L5021']          |
    | pH_Blood                        | ['A0221', 'L5017', 'A0219'] |

=== "Hepatic Panel"

    | concepts_set_name             | GLIMS_ANABIO_concept_code                     |
    |:------------------------------|:----------------------------------------------|
    | ALAT_Activity                 | ['A0002', 'G1804', 'J7373', 'E2067', 'F2629'] |
    | ASAT_Activity                 | ['A0022', 'G1800', 'E2068', 'F2628']          |
    | GGT_Activity                  | ['A0131', 'F8184', 'E9771', 'J7370', 'K7045'] |
    | PAL_Activity                  | ['A0227', 'F8187', 'E6331', 'F1844']          |
    | Total_Bilirubin_Concentration | ['A0029', 'H5264', 'D0189']                   |

=== "Cardiac Biomarkers"

    | concepts_set_name              | GLIMS_ANABIO_concept_code                                                         |
    |:-------------------------------|:----------------------------------------------------------------------------------|
    | BNP_Concentration              | ['C8189', 'B5596', 'A2128']                                                       |
    | BNP_and_NTProBNP_Concentration | ['C8189', 'B5596', 'A2128', 'A7333', 'J7267', 'J7959']                            |
    | NTProBNP_Concentration         | ['A7333', 'J7267', 'J7959']                                                       |
    | Troponine_Concentration        | ['A0283', 'C5560', 'F9934', 'E6954', 'L3534', 'G7716', 'J5184', 'A3832', 'E7249'] |

=== "Inflammatory Panel"

    | concepts_set_name            | GLIMS_ANABIO_concept_code                              |
    |:-----------------------------|:-------------------------------------------------------|
    | CRP_Concentration            | ['A0248', 'E6332', 'F5581', 'J7381', 'F2631']          |
    | Fibrinogen_Concentration     | ['A0126']                                              |
    | Proteins_Blood_Concentration | ['A7347', 'F5122', 'F2624', 'B9417', 'A0249', 'B3990'] |

=== "Martial Panel"

    | concepts_set_name                  | GLIMS_ANABIO_concept_code   |
    |:-----------------------------------|:----------------------------|
    | Ferritin_Concentration             | ['A0123', 'E9865']          |
    | Transferrin_Saturation_Coefficient | ['A0278']                   |

=== "Renal Panel"

    | concepts_set_name                  | GLIMS_ANABIO_concept_code                              |
    |:-----------------------------------|:-------------------------------------------------------|
    | Glomerular_Filtration_Rate_EPI_CKD | ['G6921', 'F8160', 'F9613', 'F9621', 'F9621']          |
    | Glomerular_Filtration_Rate_MDRD    | ['F9622', 'G7835', 'B9964', 'A7456', 'A7455', 'H5609'] |
    | Urea_Blood_Concentration           | ['A0286', 'G3350', 'J7372', 'F2620']                   |

=== "Coagulation"

    | concepts_set_name                     | GLIMS_ANABIO_concept_code                                                         |
    |:--------------------------------------|:----------------------------------------------------------------------------------|
    | Activated_Partial_Thromboplastin_Time | ['A1792', 'L7286', 'A7748']                                                       |
    | D-Dimers_Concentration                | ['C7882', 'C7882', 'I8765', 'A0124', 'C0474', 'C0474', 'C0474', 'B4199', 'F5402'] |
    | Quick_INR_Time                        | ['A0269']                                                                         |
    | Quick_Prothrombin_Time                | ['A1805', 'E9993']                                                                |

=== "Proteins"

    | concepts_set_name                | GLIMS_ANABIO_concept_code                                                                                                                          |
    |:---------------------------------|:---------------------------------------------------------------------------------------------------------------------------------------------------|
    | Albumine_Blood_Concentration     | ['D2358', 'C6841', 'C2102', 'G6616', 'L2260', 'A0006', 'E4799', 'I2013']                                                                           |
    | EPP_Blood_Concentration          | ['A0250', 'C9874', 'A3758', 'A0004', 'F9978', 'A0005', 'H8137', 'C7087', 'A0003', 'C7088', 'B9456', 'B9455', 'A0008', 'H8138', 'C7089', 'A0007'... |
    | Phosphates_Blood_Concentration   | ['A0226', 'F8186', 'F2626']                                                                                                                        |
    | Proteins_Urine_24h_Concentration | ['A1695', 'A1694', 'A1696', 'C9990', 'C9991', 'J7268', 'J7269', 'C3941', 'E4745', 'G4187', 'F6060']                                                |

=== "Diabete"

    | concepts_set_name           | GLIMS_ANABIO_concept_code                                                                                    |
    |:----------------------------|:-------------------------------------------------------------------------------------------------------------|
    | B-HCG_Blood_Concentration   | ['A7426', 'F2353', 'A0164', 'L2277']                                                                         |
    | Glucose_Blood_Concentration | ['A0141', 'H7323', 'J7401', 'F2622', 'B9553', 'C7236', 'E7312', 'A7338', 'H7324', 'C0565', 'E9889', 'A8424'] |
    | HbA1c_Blood_%               | ['B6983', 'A2228', 'A1271', 'E6632', 'I5968']                                                                |
    | TSH_Concentration           | ['A1831', 'F2150', 'I8385', 'C2666']                                                                         |

=== "Inflammatory Biomarkers"

    | concepts_set_name                 | GLIMS_ANABIO_concept_code                                                                           |
    |:----------------------------------|:----------------------------------------------------------------------------------------------------|
    | IL-1 beta_Blood_Concentration     | ['C9351', 'B8921', 'G4800', 'K3662', 'L2217', 'J9193', 'K3665', 'K3687', 'K3661', 'L2197']          |
    | IL-10_Blood_Concentration         | ['B8922', 'C8763', 'K3478', 'L2210', 'J9187', 'K3481', 'K3472', 'K3475', 'L2198']                   |
    | IL-6_Blood_Concentration          | ['B8929', 'G4799', 'B1910', 'K3467', 'L2205', 'E6992', 'J9190', 'K3456', 'L2193', 'K3435', 'K3460'] |
    | Procalcitonin_Blood_Concentration | ['A1661', 'H5267', 'F2632']                                                                         |
    | TNF alpha_Blood_Concentration     | ['B8931', 'G4801', 'C9393', 'K3505', 'L2203', 'E6993', 'J9194', 'K3658', 'K3502', 'K3504', 'L2191'] |
