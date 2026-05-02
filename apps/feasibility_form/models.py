from django.db import models

class ItemCard(models.Model):
    no = models.CharField(max_length=100, db_column='no', primary_key=True)
    customer_id = models.CharField(max_length=100, db_column='customerid')
    customer_name = models.CharField(max_length=255, db_column='customername')

    class Meta:
        db_table = "tbl_itemcard"
        managed = False   # ✅ prevents Django from trying to create/alter this legacy table


class Feasibility(models.Model):
    # initial data
    item_no = models.CharField(max_length=100, db_column='Item_No', primary_key=True)
    customer_name = models.CharField(max_length=255, db_column='CustomerName')
    enq_no = models.CharField(max_length=100, db_column='EnqNo', null=True, blank=True)
    part_name = models.CharField(max_length=255, db_column='PartName', null=True, blank=True)
    application = models.CharField(max_length=255, db_column='Application', null=True, blank=True)
    feasibility_type = models.CharField(max_length=100, db_column='FeasibilityType', null=True, blank=True)
    projected_volume = models.CharField(max_length=100, db_column='ProjectedVolume', null=True, blank=True)
    initial_date = models.DateField(db_column='InitialDate', null=True, blank=True)
    updated_on = models.DateField(db_column='UpdatedOn', null=True, blank=True)
    part_no = models.CharField(max_length=100, db_column='PartNo', null=True, blank=True)
    feasibility_no = models.CharField(max_length=100, db_column='FeasibilityNo', null=True, blank=True)
    vehicle_model = models.CharField(max_length=255, db_column='Vehicle/Model', null=True, blank=True)
    daily_peak_volumes = models.CharField(max_length=100, db_column='DailyPeakVolumes', null=True, blank=True)
    date_of_sop = models.DateField(db_column='DateofSOP', null=True, blank=True)
    AttDate = models.DateField(db_column='AttDate', null=True, blank=True)

    # Question I
    availability_customer_inter_f = models.CharField(max_length=50, db_column="Availability of Customer Inter_F")
    availability_customer_inter_r = models.CharField(max_length=50, db_column="Availability of Customer Inter_R")
    availability_customer_inter_c = models.CharField(max_length=255, db_column="Availability of Customer Inter_C")

    # Question II
    project_status_f = models.CharField(max_length=50, db_column="Does VAIPL possess the technology and engineering_F")
    project_responsible_r = models.CharField(max_length=50, db_column="Does VAIPL possess the technology and engineering_R")
    project_comments_c = models.CharField(max_length=255, db_column="Does VAIPL possess the technology and engineering_C")

    voss_status_f = models.CharField(max_length=50, db_column="RAW_Availability of tubing raw mat_F")
    voss_responsible_r = models.CharField(max_length=50, db_column="RAW_Availability of tubing raw mat_R")
    voss_comments_c = models.CharField(max_length=255, db_column="RAW_Availability of tubing raw mat_C")

    a2parts_status_f = models.CharField(max_length=50, db_column="RAW_Sourcing of raw material for B_F")
    a2parts_responsible_r = models.CharField(max_length=50, db_column="RAW_Sourcing of raw material for B_R")
    a2parts_comments_c = models.CharField(max_length=255, db_column="RAW_Sourcing of raw material for B_C") 

    a3stds_status_f = models.CharField(max_length=50, db_column="RAW_raw material specification or Stds_F")
    a3stds_responsible_r = models.CharField(max_length=50, db_column="RAW_raw material specification or Stds_R")
    a3stds_comments_c = models.CharField(max_length=255, db_column="RAW_raw material specification or Stds_C")

    source_status_f = models.CharField(max_length=50, db_column="RAW_Is there any customer designated source_F")
    source_responsible_r = models.CharField(max_length=50, db_column="RAW_Is there any customer designated source_R")
    source_comments_c = models.CharField(max_length=255, db_column="RAW_Is there any customer designated source_C")

    safety_status_f = models.CharField(max_length=50, db_column="RAW_Are product safety related characteristics_F")
    safety_responsible_r = models.CharField(max_length=50, db_column="RAW_Are product safety related characteristics_R")
    safety_comments_c = models.CharField(max_length=255, db_column="RAW_Are product safety related characteristics_C")

    export_status_f = models.CharField(max_length=50, db_column="RAW_Statutory & regulatory requirments_F")
    export_responsible_r = models.CharField(max_length=50, db_column="RAW_Statutory & regulatory requirments_R")
    export_comments_c = models.CharField(max_length=255, db_column="RAW_Statutory & regulatory requirments_C") 

    receipt_status_f = models.CharField(max_length=50, db_column="RAW_Country of receipt_F")
    receipt_responsible_r = models.CharField(max_length=50, db_column="RAW_Country of receipt_R")
    receipt_comments_c = models.CharField(max_length=255, db_column="RAW_Country of receipt_C")    

    shipment_status_f = models.CharField(max_length=50, db_column="RAW_Country of shipment_F")
    shipment_responsible_r = models.CharField(max_length=50, db_column="RAW_Country of shipment_R")
    shipment_comments_c = models.CharField(max_length=255, db_column="RAW_Country of shipment_C")




    dest_status_f = models.CharField(max_length=50, db_column="RAW_Customer identified country of destination_F")
    dest_responsible_r = models.CharField(max_length=50, db_column="RAW_Customer identified country of destination_R")
    dest_comments_c = models.CharField(max_length=255, db_column="RAW_Customer identified country of destination_C")

    legal_status_f = models.CharField(max_length=50, db_column="RAW_is applicable - Communication to HR_F")
    legal_responsible_r = models.CharField(max_length=50, db_column="RAW_is applicable - Communication to HR_R")
    legal_comments_c = models.CharField(max_length=255, db_column="RAW_is applicable - Communication to HR_C") 

    test_status_f = models.CharField(max_length=50, db_column="RAW_Feasibility of conducting test_F")
    test_responsible_r = models.CharField(max_length=50, db_column="RAW_Feasibility of conducting test_R")
    test_comments_c = models.CharField(max_length=255, db_column="RAW_Feasibility of conducting test_C")

    b_status_f = models.CharField(max_length=50, db_column="DRAW_Developing the product in the drawing/RFQ/Specs_F")
    b_responsible_r = models.CharField(max_length=50, db_column="DRAW_Developing the product in the drawing/RFQ/Specs_R")
    b_comments_c = models.CharField(max_length=255, db_column="DRAW_Developing the product in the drawing/RFQ/Specs_C")

    bsc_status_f = models.CharField(max_length=50, db_column="DRAW_Availablity of SC/CC on the drawing_F")
    bsc_responsible_r = models.CharField(max_length=50, db_column="DRAW_Availablity of SC/CC on the drawing_R")
    bsc_comments_c = models.CharField(max_length=255, db_column="DRAW_Availablity of SC/CC on the drawing_C")

    data_status_f = models.CharField(max_length=50, db_column="DRAW_information/data for sourcing B/O_F")
    data_responsible_r = models.CharField(max_length=50, db_column="DRAW_information/data for sourcing B/O_R")
    data_comments_c = models.CharField(max_length=255, db_column="DRAW_information/data for sourcing B/O_C")   

    surface_status_f = models.CharField(max_length=50, db_column="DRAW_Surface finish/painting/coatings for B/O components_F")
    surface_responsible_r = models.CharField(max_length=50, db_column="DRAW_Surface finish/painting/coatings for B/O components_R")
    surface_comments_c = models.CharField(max_length=255, db_column="DRAW_Surface finish/painting/coatings for B/O components_C")

    method_status_f = models.CharField(max_length=50, db_column="DRAW_Feasibility of conducting functional tests specified_F")
    method_responsible_r = models.CharField(max_length=50, db_column="DRAW_Feasibility of conducting functional tests specified_R")
    method_comments_c = models.CharField(max_length=255, db_column="DRAW_Feasibility of conducting functional tests specified_C")



    c1_status_f = models.CharField(max_length=50, db_column="MAN_Feasibility of achieving the product tolerances_F")
    c1_responsible_r = models.CharField(max_length=50, db_column="MAN_Feasibility of achieving the product tolerances_R")
    c1_comments_c = models.CharField(max_length=255, db_column="MAN_Feasibility of achieving the product tolerances_C")

    c2_status_f = models.CharField(max_length=50, db_column="MAN_Achievability of CP/CPk >167 wherever SC/CC_F")
    c2_responsible_r = models.CharField(max_length=50, db_column="MAN_Achievability of CP/CPk >167 wherever SC/CC_R")
    c2_comments_c = models.CharField(max_length=255, db_column="MAN_Achievability of CP/CPk >167 wherever SC/CC_C")

    c3_status_f = models.CharField(max_length=50, db_column="MAN_Any new processing facility required_F")
    c3_responsible_r = models.CharField(max_length=50, db_column="MAN_Any new processing facility required_R")
    c3_comments_c = models.CharField(max_length=255, db_column="MAN_Any new processing facility required_C")   

    c4_status_f = models.CharField(max_length=50, db_column="MAN_Requirement of any special Jigs_F")
    c4_responsible_r = models.CharField(max_length=50, db_column="MAN_Requirement of any special Jigs_R")
    c4_comments_c = models.CharField(max_length=255, db_column="MAN_Requirement of any special Jigs_C")

    c5_status_f = models.CharField(max_length=50, db_column="MAN_Manufacturing feasibility of Jigs/Fixtures_F")
    c5_responsible_r = models.CharField(max_length=50, db_column="MAN_Manufacturing feasibility of Jigs/Fixtures_R")
    c5_comments_c = models.CharField(max_length=255, db_column="MAN_Manufacturing feasibility of Jigs/Fixtures_C")


    d1_status_f = models.CharField(max_length=50, db_column="CAP_Former Mfg Capacity_F")
    d1_responsible_r = models.CharField(max_length=50, db_column="CAP_Former Mfg Capacity_R")
    d1_comments_c = models.CharField(max_length=255, db_column="CAP_Former Mfg Capacity_C")

    d2_status_f = models.CharField(max_length=50, db_column="CAP_Chk/Bundle Fix Mfg Capacity_F")
    d2_responsible_r = models.CharField(max_length=50, db_column="CAP_Chk/Bundle Fix Mfg Capacity_R")
    d2_comments_c = models.CharField(max_length=255, db_column="CAP_Chk/Bundle Fix Mfg Capacity_C")

    d3_status_f = models.CharField(max_length=50, db_column="CAP_Forming Capacity_F")
    d3_responsible_r = models.CharField(max_length=50, db_column="CAP_Forming Capacity_R")
    d3_comments_c = models.CharField(max_length=255, db_column="CAP_Forming Capacity_C")   

    d4_status_f = models.CharField(max_length=50, db_column="CAP_Production Capacity Cell Manpower_F")
    d4_responsible_r = models.CharField(max_length=50, db_column="CAP_Production Capacity Cell Manpower_R")
    d4_comments_c = models.CharField(max_length=255, db_column="CAP_Production Capacity Cell Manpower_C")

    d5_status_f = models.CharField(max_length=50, db_column="CAP_B/O Part sourcing-Supplier Capacity_F")
    d5_responsible_r = models.CharField(max_length=50, db_column="CAP_B/O Part sourcing-Supplier Capacity_R")
    d5_comments_c = models.CharField(max_length=255, db_column="CAP_B/O Part sourcing-Supplier Capacity_C") 




    e1_status_f = models.CharField(max_length=50, db_column="INSP_Feasibility of checking SC/CC_F")
    e1_responsible_r = models.CharField(max_length=50, db_column="INSP_Feasibility of checking SC/CC_R")
    e1_comments_c = models.CharField(max_length=255, db_column="INSP_Feasibility of checking SC/CC_C")

    e2_status_f = models.CharField(max_length=50, db_column="INSP_Any Special Inspection equipment_F")
    e2_responsible_r = models.CharField(max_length=50, db_column="INSP_Any Special Inspection equipment_R")
    e2_comments_c = models.CharField(max_length=255, db_column="INSP_Any Special Inspection equipment_C")

    e3_status_f = models.CharField(max_length=50, db_column="INSP_List the dimensions associated with SC/CC_F")
    e3_responsible_r = models.CharField(max_length=50, db_column="INSP_List the dimensions associated with SC/CC_R")
    e3_comments_c = models.CharField(max_length=255, db_column="INSP_List the dimensions associated with SC/CC_C")

    f1_status_f = models.CharField(max_length=50, db_column="TEST_Requirement of Functional /Endurance_F")
    f1_responsible_r = models.CharField(max_length=50, db_column="TEST_Requirement of Functional /Endurance_R")
    f1_comments_c = models.CharField(max_length=255, db_column="TEST_Requirement of Functional /Endurance_C")

    f2_status_f = models.CharField(max_length=50, db_column="TEST_Are DVP tests required_F")
    f2_responsible_r = models.CharField(max_length=50, db_column="TEST_Are DVP tests required_R")
    f2_comments_c = models.CharField(max_length=255, db_column="TEST_Are DVP tests required_C")

    f3_status_f = models.CharField(max_length=50, db_column="TEST_Identify sources for conducting tests_F")
    f3_responsible_r = models.CharField(max_length=50, db_column="TEST_Identify sources for conducting tests_R")
    f3_comments_c = models.CharField(max_length=255, db_column="TEST_Identify sources for conducting tests_C")

    g1_status_f = models.CharField(max_length=50, db_column="CUST_Feasibility of achieving any customer_F")
    g1_responsible_r = models.CharField(max_length=50, db_column="CUST_Feasibility of achieving any customer_R")
    g1_comments_c = models.CharField(max_length=255, db_column="CUST_Feasibility of achieving any customer_C")

    g2_status_f = models.CharField(max_length=50, db_column="CUST_Requirement of customer regarding_F")
    g2_responsible_r = models.CharField(max_length=50, db_column="CUST_Requirement of customer regarding_R")
    g2_comments_c = models.CharField(max_length=255, db_column="CUST_Requirement of customer regarding_C")

    g3_status_f = models.CharField(max_length=50, db_column="CUST_Need identification/updating skill matrix_F")
    g3_responsible_r = models.CharField(max_length=50, db_column="CUST_Need identification/updating skill matrix_R")
    g3_comments_c = models.CharField(max_length=255, db_column="CUST_Need identification/updating skill matrix_C")

    h1_status_f = models.CharField(max_length=50, db_column="EXP_Availability of existing projects very similar_F")
    h1_responsible_r = models.CharField(max_length=50, db_column="EXP_Availability of existing projects very similar_R")
    h1_comments_c = models.CharField(max_length=255, db_column="EXP_Availability of existing projects very similar_C")

    h2_status_f = models.CharField(max_length=50, db_column="EXP_Reference of TGR/TGW/G8D/Complaint_F")
    h2_responsible_r = models.CharField(max_length=50, db_column="EXP_Reference of TGR/TGW/G8D/Complaint_R")
    h2_comments_c = models.CharField(max_length=255, db_column="EXP_Reference of TGR/TGW/G8D/Complaint_C")

    h3_status_f = models.CharField(max_length=50, db_column="EXP_Refer PROJECT GUIDELINES\Mgidcsrv01\quality_F")
    h3_responsible_r = models.CharField(max_length=50, db_column="EXP_Refer PROJECT GUIDELINES\Mgidcsrv01\quality_R")
    h3_comments_c = models.CharField(max_length=255, db_column="EXP_Refer PROJECT GUIDELINES\Mgidcsrv01\quality_C")  


    i1_status_f = models.CharField(max_length=50, db_column="ENV_Is Aspect & Impact Study required_F")
    i1_responsible_r = models.CharField(max_length=50, db_column="ENV_Is Aspect & Impact Study required_R")
    i1_comments_c = models.CharField(max_length=255, db_column="ENV_Is Aspect & Impact Study required_C")

    i2_status_f = models.CharField(max_length=50, db_column="ENV_If Yes, Are there Significant Aspect_F")
    i2_responsible_r = models.CharField(max_length=50, db_column="ENV_If Yes, Are there Significant Aspect_R")
    i2_comments_c = models.CharField(max_length=255, db_column="ENV_If Yes, Are there Significant Aspect_C")

    i3_status_f = models.CharField(max_length=50, db_column="ENV_If Yes, What is the control of Significant Aspects_F")
    i3_responsible_r = models.CharField(max_length=50, db_column="ENV_If Yes, What is the control of Significant Aspects_R")
    i3_comments_c = models.CharField(max_length=255, db_column="ENV_If Yes, What is the control of Significant Aspects_C")   

    i4_status_f = models.CharField(max_length=50, db_column="ENV_Is there any additioal Legal requirements_F")
    i4_responsible_r = models.CharField(max_length=50, db_column="ENV_Is there any additioal Legal requirements_R")
    i4_comments_c = models.CharField(max_length=255, db_column="ENV_Is there any additioal Legal requirements_C")

    i5_status_f = models.CharField(max_length=50, db_column="ENV_Compliance to Legal requirements_F")
    i5_responsible_r = models.CharField(max_length=50, db_column="ENV_Compliance to Legal requirements_R")
    i5_comments_c = models.CharField(max_length=255, db_column="ENV_Compliance to Legal requirements_C")  

    i6_status_f = models.CharField(max_length=50, db_column="ENV_Availability of MSDS_F")
    i6_responsible_r = models.CharField(max_length=50, db_column="ENV_Availability of MSDS_R")
    i6_comments_c = models.CharField(max_length=255, db_column="ENV_Availability of MSDS_C")   

    i7_status_f = models.CharField(max_length=50, db_column="ENV_RequirmentRelatedToEMS_F")
    i7_responsible_r = models.CharField(max_length=50, db_column="ENV_RequirmentRelatedToEMS_R")
    i7_comments_c = models.CharField(max_length=255, db_column="ENV_RequirmentRelatedToEMS_C")


    final1_status_f = models.CharField(max_length=50, db_column="ENV_Product can be produced as specified_F")
    final1_responsible_r = models.CharField(max_length=50, db_column="ENV_Product can be produced as specified_R")
    final1_comments_c = models.CharField(max_length=255, db_column="ENV_Product can be produced as specified_C")

    final2_status_f = models.CharField(max_length=50, db_column="ENV_Changes recommended_F")
    final2_responsible_r = models.CharField(max_length=50, db_column="ENV_Changes recommended_R")
    final2_comments_c = models.CharField(max_length=255, db_column="ENV_Changes recommended_C")

    final3_status_f = models.CharField(max_length=50, db_column="EVN_Design revision required to produce_F")
    final3_responsible_r = models.CharField(max_length=50, db_column="EVN_Design revision required to produce_R")
    final3_comments_c = models.CharField(max_length=255, db_column="EVN_Design revision required to produce_C") 


    marketing_attendance = models.CharField(max_length=50, db_column="Marketing")
    materials_attendance = models.CharField(max_length=50, db_column="Materials")
    quality_attendance = models.CharField(max_length=255, db_column="Quality")
    pe_attendance = models.CharField(max_length=50, db_column="PE")
    me_attendance = models.CharField(max_length=50, db_column="ME")
    pm_attendance = models.CharField(max_length=255, db_column="PDPM")
 

    class Meta:
        db_table = "tbl_feasibility"
        managed = False
