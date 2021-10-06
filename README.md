# Python_Automation_Regex

This is a simple program that uses Regular Expressions

#Input
assign ANA_I_ZQCAL_zqcal_amux_sel[1:0] = db.I_ZQCAL.amux_sel[1:0];
assign ANA_I_BCOM_bcom_vref_amux_en = db.I_BCOM.vref_mux_en;
#Output
A_WIRE_WRAP#(2) ANA_I_ZQCAL_zqcal_amux_sel_wrapper(.IN(db.I_ZQCAL.amux_sel), .OUT(ANA_I_ZQCAL_zqcal_amux_sel));
A_WIRE_WRAP#(1) ANA_I_BCOM_bcom_vref_amux_en_wrapper(.IN(db.I_BCOM.vref_mux_en), .OUT(ANA_I_BCOM_bcom_vref_amux_en));
