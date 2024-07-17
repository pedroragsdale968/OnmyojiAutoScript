from module.atom.image import RuleImage
from module.atom.click import RuleClick
from module.atom.long_click import RuleLongClick
from module.atom.swipe import RuleSwipe
from module.atom.ocr import RuleOcr
from module.atom.list import RuleList

# This file was automatically generated by ./dev_tools/assets_extract.py.
# Don't modify it manually.
class RyouToppaAssets: 


	# Click Rule Assets
	# area1 
	C_AREA_1 = RuleClick(roi_front=(533,162,177,74), roi_back=(533,162,177,74), name="area_1")
	# area2 
	C_AREA_2 = RuleClick(roi_front=(863,164,181,71), roi_back=(863,164,181,71), name="area_2")
	# area3 
	C_AREA_3 = RuleClick(roi_front=(532,292,181,87), roi_back=(532,292,181,87), name="area_3")
	# area4 
	C_AREA_4 = RuleClick(roi_front=(863,301,171,62), roi_back=(863,301,171,62), name="area_4")
	# area5 
	C_AREA_5 = RuleClick(roi_front=(540,432,169,68), roi_back=(540,432,169,68), name="area_5")
	# area6 
	C_AREA_6 = RuleClick(roi_front=(876,432,165,74), roi_back=(876,432,165,74), name="area_6")
	# area7 
	C_AREA_7 = RuleClick(roi_front=(538,557,149,71), roi_back=(538,557,149,71), name="area_7")
	# area8 
	C_AREA_8 = RuleClick(roi_front=(876,562,150,67), roi_back=(876,562,150,67), name="area_8")
	# 在点击进攻后如果未进入战斗画面则点击的安全区域 
	C_SAFE_AREA = RuleClick(roi_front=(182,213,160,229), roi_back=(182,213,160,229), name="safe_area")


	# Image Rule Assets
	# 区域1攻略失败 
	I_AREA_1_IS_FAILURE = RuleImage(roi_front=(673,146,63,32), roi_back=(421,127,325,134), threshold=0.8, method="Template matching", file="./tasks/RyouToppa/dev/loser_sign_1.png")
	# 区域2攻略失败 
	I_AREA_2_IS_FAILURE = RuleImage(roi_front=(1011,146,63,30), roi_back=(757,125,327,140), threshold=0.8, method="Template matching", file="./tasks/RyouToppa/dev/loser_sign_1.png")
	# 区域3攻略失败 
	I_AREA_3_IS_FAILURE = RuleImage(roi_front=(665,283,73,40), roi_back=(419,254,327,144), threshold=0.8, method="Template matching", file="./tasks/RyouToppa/dev/loser_sign_1.png")
	# 区域4攻略失败 
	I_AREA_4_IS_FAILURE = RuleImage(roi_front=(1000,283,72,38), roi_back=(756,260,325,139), threshold=0.8, method="Template matching", file="./tasks/RyouToppa/dev/loser_sign_1.png")
	# 区域5攻略失败 
	I_AREA_5_IS_FAILURE = RuleImage(roi_front=(669,419,65,29), roi_back=(418,392,328,142), threshold=0.8, method="Template matching", file="./tasks/RyouToppa/dev/loser_sign_1.png")
	# 区域6攻略失败 
	I_AREA_6_IS_FAILURE = RuleImage(roi_front=(988,416,84,37), roi_back=(755,395,328,141), threshold=0.8, method="Template matching", file="./tasks/RyouToppa/dev/loser_sign_1.png")
	# 区域7攻略失败 
	I_AREA_7_IS_FAILURE = RuleImage(roi_front=(672,556,61,37), roi_back=(420,530,326,127), threshold=0.8, method="Template matching", file="./tasks/RyouToppa/dev/loser_sign_1.png")
	# 区域8攻略失败 
	I_AREA_8_IS_FAILURE = RuleImage(roi_front=(1004,556,64,29), roi_back=(756,530,327,124), threshold=0.8, method="Template matching", file="./tasks/RyouToppa/dev/loser_sign_1.png")
	# 区域1攻略失败（最近一次） 
	I_AREA_1_IS_FAILURE_NEW = RuleImage(roi_front=(673,146,63,32), roi_back=(421,123,325,138), threshold=0.8, method="Template matching", file="./tasks/RyouToppa/dev/loser_sign_2.png")
	# 区域2攻略失败（最近一次） 
	I_AREA_2_IS_FAILURE_NEW = RuleImage(roi_front=(1011,146,63,30), roi_back=(757,126,327,139), threshold=0.8, method="Template matching", file="./tasks/RyouToppa/dev/loser_sign_2.png")
	# 区域3攻略失败（最近一次） 
	I_AREA_3_IS_FAILURE_NEW = RuleImage(roi_front=(665,283,73,40), roi_back=(419,261,327,137), threshold=0.8, method="Template matching", file="./tasks/RyouToppa/dev/loser_sign_2.png")
	# 区4攻略失败（最近一次） 
	I_AREA_4_IS_FAILURE_NEW = RuleImage(roi_front=(1000,283,72,38), roi_back=(756,258,325,141), threshold=0.8, method="Template matching", file="./tasks/RyouToppa/dev/loser_sign_2.png")
	# 区域5攻略失败（最近一次） 
	I_AREA_5_IS_FAILURE_NEW = RuleImage(roi_front=(669,419,65,29), roi_back=(418,394,328,140), threshold=0.8, method="Template matching", file="./tasks/RyouToppa/dev/loser_sign_2.png")
	# 区域6攻略失败（最近一次） 
	I_AREA_6_IS_FAILURE_NEW = RuleImage(roi_front=(988,416,84,37), roi_back=(755,395,328,141), threshold=0.8, method="Template matching", file="./tasks/RyouToppa/dev/loser_sign_2.png")
	# 区域7攻略失败（最近一次） 
	I_AREA_7_IS_FAILURE_NEW = RuleImage(roi_front=(672,556,61,37), roi_back=(420,533,326,124), threshold=0.8, method="Template matching", file="./tasks/RyouToppa/dev/loser_sign_2.png")
	# 区域8攻略失败（最近一次） 
	I_AREA_8_IS_FAILURE_NEW = RuleImage(roi_front=(1004,556,64,29), roi_back=(756,532,327,122), threshold=0.8, method="Template matching", file="./tasks/RyouToppa/dev/loser_sign_2.png")


	# Image Rule Assets
	# 区域1已攻破 
	I_AREA_1_FINISHED = RuleImage(roi_front=(658,141,93,91), roi_back=(421,127,325,134), threshold=0.8, method="Template matching", file="./tasks/RyouToppa/dev/finished_1.png")
	# 区域2已攻破 
	I_AREA_2_FINISHED = RuleImage(roi_front=(983,137,100,100), roi_back=(757,125,327,140), threshold=0.8, method="Template matching", file="./tasks/RyouToppa/dev/finished_1.png")
	# 区域3已攻破 
	I_AREA_3_FINISHED = RuleImage(roi_front=(681,312,47,37), roi_back=(419,254,327,144), threshold=0.8, method="Template matching", file="./tasks/RyouToppa/dev/finished_1.png")
	# 区域4已攻破 
	I_AREA_4_FINISHED = RuleImage(roi_front=(996,271,100,100), roi_back=(756,260,325,139), threshold=0.8, method="Template matching", file="./tasks/RyouToppa/dev/finished_1.png")
	# 区域5已攻破 
	I_AREA_5_FINISHED = RuleImage(roi_front=(647,404,100,100), roi_back=(418,392,328,142), threshold=0.8, method="Template matching", file="./tasks/RyouToppa/dev/finished_1.png")
	# 区域6已攻破 
	I_AREA_6_FINISHED = RuleImage(roi_front=(1015,448,56,35), roi_back=(755,395,328,141), threshold=0.8, method="Template matching", file="./tasks/RyouToppa/dev/finished_1.png")
	# 区域7已攻破 
	I_AREA_7_FINISHED = RuleImage(roi_front=(643,543,100,100), roi_back=(420,530,326,127), threshold=0.8, method="Template matching", file="./tasks/RyouToppa/dev/finished_1.png")
	# 区域8已攻破 
	I_AREA_8_FINISHED = RuleImage(roi_front=(983,541,100,100), roi_back=(756,530,327,124), threshold=0.8, method="Template matching", file="./tasks/RyouToppa/dev/finished_1.png")
	# 区域1已攻破新 
	I_AREA_1_FINISHED_NEW = RuleImage(roi_front=(658,141,93,91), roi_back=(421,127,325,134), threshold=0.8, method="Template matching", file="./tasks/RyouToppa/dev/finished_2.png")
	# 区域2已攻破新 
	I_AREA_2_FINISHED_NEW = RuleImage(roi_front=(983,137,100,100), roi_back=(757,125,327,140), threshold=0.8, method="Template matching", file="./tasks/RyouToppa/dev/finished_2.png")
	# 区域3已攻破新 
	I_AREA_3_FINISHED_NEW = RuleImage(roi_front=(681,312,47,37), roi_back=(419,254,327,144), threshold=0.8, method="Template matching", file="./tasks/RyouToppa/dev/finished_2.png")
	# 区域4已攻破新 
	I_AREA_4_FINISHED_NEW = RuleImage(roi_front=(996,271,100,100), roi_back=(756,260,325,139), threshold=0.8, method="Template matching", file="./tasks/RyouToppa/dev/finished_2.png")
	# 区域5已攻破新 
	I_AREA_5_FINISHED_NEW = RuleImage(roi_front=(647,404,100,100), roi_back=(418,392,328,142), threshold=0.8, method="Template matching", file="./tasks/RyouToppa/dev/finished_2.png")
	# 区域6已攻破新 
	I_AREA_6_FINISHED_NEW = RuleImage(roi_front=(1015,448,56,35), roi_back=(755,395,328,141), threshold=0.8, method="Template matching", file="./tasks/RyouToppa/dev/finished_2.png")
	# 区域7已攻破新 
	I_AREA_7_FINISHED_NEW = RuleImage(roi_front=(643,543,100,100), roi_back=(420,530,326,127), threshold=0.8, method="Template matching", file="./tasks/RyouToppa/dev/finished_2.png")
	# 区域8已攻破新 
	I_AREA_8_FINISHED_NEW = RuleImage(roi_front=(983,541,100,100), roi_back=(756,530,327,124), threshold=0.8, method="Template matching", file="./tasks/RyouToppa/dev/finished_2.png")


	# Image Rule Assets
	# description 
	I_TOPPA_RECORD = RuleImage(roi_front=(66,628,64,39), roi_back=(66,628,64,39), threshold=0.8, method="Template matching", file="./tasks/RyouToppa/dev/res_toppa_record.png")
	# description 
	I_TOPPA_LOCK_TEAM = RuleImage(roi_front=(203,602,26,32), roi_back=(203,602,26,32), threshold=0.8, method="Template matching", file="./tasks/RyouToppa/dev/dev_toppa_lock_team.png")
	# description 
	I_TOPPA_UNLOCK_TEAM = RuleImage(roi_front=(202,603,25,31), roi_back=(202,603,25,31), threshold=0.8, method="Template matching", file="./tasks/RyouToppa/dev/dev_toppa_unlock_team.png")


	# Click Rule Assets
	# 选择第一个寮 
	C_SELECT_FIRST_RYOU = RuleClick(roi_front=(1148,138,21,22), roi_back=(1148,138,21,22), name="select_first_ryou")


	# Image Rule Assets
	# 寮突 
	I_RYOU_TOPPA = RuleImage(roi_front=(1191,352,78,116), roi_back=(1161,323,118,193), threshold=0.6, method="Template matching", file="./tasks/RyouToppa/res/res_ryou_toppa.png")
	# 寮突选择阴阳寮按钮 
	I_SELECT_RYOU_BUTTON = RuleImage(roi_front=(560,577,156,46), roi_back=(560,577,156,46), threshold=0.8, method="Template matching", file="./tasks/RyouToppa/res/res_select_ryou_button.png")
	# 开始寮突按钮 
	I_START_TOPPA_BUTTON = RuleImage(roi_front=(832,279,130,43), roi_back=(1,1,1055,718), threshold=0.8, method="Template matching", file="./tasks/RyouToppa/res/res_start_toppa_button.png")
	# 寮击破奖励 
	I_RYOU_REWARD = RuleImage(roi_front=(134,417,241,40), roi_back=(134,417,241,40), threshold=0.8, method="Template matching", file="./tasks/RyouToppa/res/res_ryou_reward.png")
	# 勋章奖励标题 
	I_GUILD_ORDERS_REWARDS = RuleImage(roi_front=(1123,31,115,56), roi_back=(1123,31,115,56), threshold=0.8, method="Template matching", file="./tasks/RyouToppa/res/res_guild_orders_rewards.png")
	# 攻破阴阳寮 
	I_SUCCESS_PENETRATION = RuleImage(roi_front=(141,374,234,37), roi_back=(141,374,234,37), threshold=0.8, method="Template matching", file="./tasks/RyouToppa/res/res_success_penetration.png")
	# 个人突破刷新按钮 
	I_REAL_RAID_REFRESH = RuleImage(roi_front=(963,569,174,60), roi_back=(963,569,174,60), threshold=0.8, method="Template matching", file="./tasks/RyouToppa/res/res_real_raid_refresh.png")
	# 击破后的寮奖励 
	I_RYOU_REWARD_90 = RuleImage(roi_front=(134,415,232,38), roi_back=(134,415,232,38), threshold=0.8, method="Template matching", file="./tasks/RyouToppa/res/res_ryou_reward_90.png")


	# Ocr Rule Assets
	# 寮突破进攻机会数 
	O_NUMBER = RuleOcr(roi=(271,560,48,31), area=(271,560,48,31), mode="DigitCounter", method="Default", keyword="", name="number")


