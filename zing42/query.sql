create table comData as select a.*,b.`NAME_OF_COMPANY`,b.`DATE_OF_LISTING`,b.`PAID_UP_VALUE`,b.`MARKET_LOT`, b.`ISIN_NUMBER`,b.`FACE_VALUE` from bhavcopy a, mytable b where a.symbol = b.symbol ;
SELECT * FROM COMdATA;

create table close_latest as select symbol,close from MONTHLYDATA where TIMESTAMP='08-DEC-2022';
create table open_oldest select symbol,open from MONTHLYDATA where TIMESTAMP='09-NOV-2022';


select a.* , b.open from close_latest a,open_oldest b where a.symbol = b.symbol;
