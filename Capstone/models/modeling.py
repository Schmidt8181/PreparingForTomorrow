import pyflux as pf


def VAR_model(df, target, lags, differences):
    VAR_model = pf.VAR(data=df, target=target, lags=lags, integ=differences)
    VARx = VAR_model.fit()
    print(VARx.summary())
    #VAR_model.plot_z(list(range(0,6)),figsize=(15,5))
    #VAR_model.plot_fit(figsize=(15,5))
    #VAR_model.plot_predict(past_values=19, h=5, figsize=(15,5))
    #VAR_model.plot_predict_is(h=10, figsize=((15,5)))

def ARIMAX_model(df, target, ar, integ, ma):
    pfarima_model = pf.ARIMA(data=df, ar=ar, ma=ma, integ=integ, target=target, family=pf.Normal())
    arima_x_mh = pfarima_model.fit("M-H")
    arima_x_mh.summary()
    #pfarima_model.plot_z(figsize=(15,5))
    #pfarima_model.plot_fit(figsize=(15,10))
    #pfarima_model.plot_predict_is(h=50, figsize=(15,5))