BEGIN TRANSACTION;
CREATE TABLE IF NOT EXISTS "equip" (
	"equip_uid"	int pk, increment,
	"ATK_N"	int,
	"AATK"	int,
	"DEF_N"	int,
	"DDEF"	int,
	"HP_N"	int,
	"HHP"	int,
	"SPD"	int,
	"CC"	int,
	"CD"	int,
	"EF"	int,
	"ER"	int,
	"TV"	int
);
COMMIT;
