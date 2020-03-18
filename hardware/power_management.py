#
# 電源管理.
#

##################################################
# import
##################################################
import lcd
import pmu

##################################################
# initialize
##################################################
# LCDを初期化
lcd.init()
# LCDの方向を設定
lcd.direction(lcd.YX_LRUD)

##################################################
# main
##################################################
# axp192オブジェクトを取得
axp = pmu.axp192()
axp.enableADCs(True)

while True:
    # 電源情報を取得
    # バッテリー電圧
    vbat = axp.getVbatVoltage()
    # USB電源電圧
    usb_vol = axp.getUSBVoltage()
    # USB電源電流
    usb_cur = axp.getUSBInputCurrent()
    # 外部電源電圧
    connext_vol = axp.getConnextVoltage()
    # 外部電源電流
    connext_input_current = axp.getConnextInputCurrent()
    # バッテリー充電電流
    bat_current = axp.getBatteryChargeCurrent()
    # バッテリー放電電流
    bat_dis_current = axp.getBatteryDischargeCurrent()
    # バッテリー消費電力
    bat_instant_watts = axp.getBatteryInstantWatts()
    # 温度
    temp = axp.getTemperature()

    # 取得した情報をLCDに描画
    lcd.draw_string(10, 5, "usb_vol: %.2fmV" % usb_vol)
    lcd.draw_string(10, 20, "usb_cur: %.2fmA" % usb_cur)
    lcd.draw_string(10, 35, "connext_vol: %.2fmV" % connext_vol)
    lcd.draw_string(10, 50, "bat_vol: %.2fmV" % vbat)
    lcd.draw_string(10, 65, "bat_current: %.2fmA" % bat_current)
    lcd.draw_string(10, 80, "bat_dis_current: %.2fmA" % bat_dis_current)
    lcd.draw_string(10, 95, "bat_instant_watts: %.2fmW" % bat_instant_watts)
    lcd.draw_string(10, 110, "temperature: %.2fC" % temp)
