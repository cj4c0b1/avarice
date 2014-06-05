import genconfig
import indicators

# This file is not to be edited like genconfig is

# OKCoin minimum asset trade values
if genconfig.TradePair == 'btc_cny':
    AssetTradeMin = 0.01
elif genconfig.TradePair == 'ltc_cny':
    AssetTradeMin = 0.1

# Due to external calling and varying indicator types,
# we can't use concat or getattr here.
# BidAskList is used to determine if Bid and Ask are lists.
# BidAskReverse is used to determine if Bid and Ask trades
# should be reversed (useful for diff trend trading)
if genconfig.Indicator == 'EMACD':
    BidAskList = True
    TradeReverse = False
    IndicatorList = indicators.EMAShort_list
    IndicatorBid = indicators.EMALong_list
    IndicatorAsk = IndicatorBid
if genconfig.Indicator == 'EMADiff':
    BidAskList = False
    TradeReverse = True
    IndicatorList = indicators.EMADiff_list
    IndicatorBid = genconfig.EMADiffUp
    IndicatorAsk = genconfig.EMADiffDown
elif genconfig.Indicator == 'RSI':
    BidAskList = False
    TradeReverse = False
    IndicatorList = indicators.RSI_list
    IndicatorAsk = genconfig.RSIAsk
    IndicatorBid = genconfig.RSIBid
elif genconfig.Indicator == 'FastStochRSIK':
    BidAskList = False
    TradeReverse = False
    IndicatorList = indicators.FastStochRSIK_list
    IndicatorAsk = genconfig.FastStochRSIKAsk
    IndicatorBid = genconfig.FastStochRSIKBid
elif genconfig.Indicator == 'FastStochRSID':
    BidAskList = False
    TradeReverse = False
    IndicatorList = indicators.FastStochRSID_list
    IndicatorAsk = genconfig.FastStochRSIDAsk
    IndicatorBid = genconfig.FastStochRSIDBid
elif genconfig.Indicator == 'FullStochRSID':
    BidAskList = False
    TradeReverse = False
    IndicatorList = indicators.FullStochRSID_list
    IndicatorAsk = genconfig.FullStochRSIDAsk
    IndicatorBid = genconfig.FullStochRSIDBid
elif genconfig.Indicator == 'FastStochK':
    BidAskList = False
    TradeReverse = False
    IndicatorList = indicators.FastStochK_list
    IndicatorAsk = genconfig.FastStochKAsk
    IndicatorBid = genconfig.FastStochKBid
elif genconfig.Indicator == 'FastStochD':
    BidAskList = False
    TradeReverse = False
    IndicatorList = indicators.FastStochD_list
    IndicatorAsk = genconfig.FastStochDAsk
    IndicatorBid = genconfig.FastStochDBid
elif genconfig.Indicator == 'FullStochD':
    BidAskList = False
    TradeReverse = False
    IndicatorList = indicators.FullStochD_list
    IndicatorAsk = genconfig.FullStochDAsk
    IndicatorBid = genconfig.FullStochDBid