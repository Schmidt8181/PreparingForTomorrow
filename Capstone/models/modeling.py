import pyflux as pf


def VAR_model(df, lags, differences):
    VAR_model = pf.VAR(data=df, lags=lags, integ=differences)
    VARx = VAR_model.fit()
    print(VARx.summary())
    VAR_model.plot_z(list(range(0,6)),figsize=(15,5))
    VAR_model.plot_fit(figsize=(15,5))
    VAR_model.plot_predict(past_values=19, h=5, figsize=(15,5))
    VAR_model.plot_predict_is(h=10, figsize=((15,5)))

def ARIMAX_model(df, target):
    pfarima_model = pf.ARIMA(data=df, ar=4, ma=4, target=target, family=pf.Normal())
    arima_x = pfarima_model.fit("MLE")
    arima_x.summary()
    arima_x_mh = pfarima_model.fit("M-H")
    arima_x_mh.summary()
    pfarima_model.plot_z(figsize=(15,5))
    pfarima_model.plot_fit(figsize=(15,10))
    pfarima_model.plot_predict_is(h=50, figsize=(15,5))

# next model type here
def 
# last model type here
