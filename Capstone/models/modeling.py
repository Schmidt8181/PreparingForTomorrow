import pyflux as pf

from sklearn.metrics import mean_squared_error
from statsmodels.tsa.arima_model import ARIMA
from statsmodels.tsa.arima_model import ARIMAResults

def evaluate_arima_model(X, arima_order):
    # prepare training dataset
    train_size = int(len(X) * 0.66)
    train, test = X[0:train_size], X[train_size:]
    history = [x for x in train]
    # make predictions
    predictions = list()
    for t in range(len(test)):
        model = ARIMA(history, order=arima_order)
        model_fit = model.fit(disp=0)
        yhat = model_fit.forecast()[0]
        predictions.append(yhat)
        history.append(test[t])
    # calculate out of sample error
    error = mean_squared_error(test, predictions)
    return error

def evaluate_models(dataset, p_values, d_values, q_values):
    dataset = dataset.astype('float32')
    best_score, best_cfg = float("inf"), None
    for p in p_values:
        for d in d_values:
            for q in q_values:
                order = (p,d,q)
                try:
                    mse = evaluate_arima_model(dataset, order)
                    if mse < best_score:
                        best_score, best_cfg = mse, order
                    print('ARIMA%s MSE=%.3f' % (order,mse))
                except:
                    continue
    print('Best ARIMA%s MSE=%.3f' % (best_cfg, best_score))

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
