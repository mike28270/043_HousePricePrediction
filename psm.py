import pandas as pd
import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt
import math
from scipy.stats import skew
from scipy.stats import kurtosis
from fitter import Fitter, get_common_distributions, get_distributions
from scipy.stats import lognorm
from scipy.stats import expon
from scipy.stats import weibull_min
from scipy.stats import poisson
from scipy.stats import norm
from pandas.core.dtypes.common import is_numeric_dtype
from pandas.core.dtypes.common import is_string_dtype
from pandas.api.types import CategoricalDtype


def plotpdf(df, x, ax, kde=True, title='Histrogram and pdf of {}.'):
    df_temp = df.copy()
    def annotate(**kws):
        value = psm.distributionValue(df_temp[x])
        annotate_value = 'mean: {:0.2f}\nstd: {:0.2f}\nskew: {:0.2f}\nkurt: {:0.2f}'.format(value['mean'],value['std'],value['skewness'],value['kurtosis'])
        #ax = plt.gca()
        if value['skewness'] < 0:
            x_anotate = 0.05
        else:
            x_anotate = 0.7
        ax.annotate(annotate_value, xy=(x_anotate, .6), xycoords=ax.transAxes)

    sns.histplot(df_temp, x=x, kde=kde, ax=ax)
    ax.set_title(title.format(x))
    ax.tick_params(axis='x', rotation=0)
    plt.tight_layout()
    annotate()
    return ax

def findNumerical(df, show=True):
    df_temp = df.copy()
    numerical_list = []
    for column in df_temp.columns.values:
        is_num = is_numeric_dtype(df_temp[column])
        if is_num is True:
            numerical_list.append(column)
            if show is True:
                print('{} : {}'.format(column, is_num))
    return numerical_list

def findMissingRows(df, show='missing'):
    df_temp = df.copy()
    all_percent_series = (df_temp.isnull().sum()/df_temp.shape[0])*100
    if show == 'all':
        return all_percent_series
    elif show == 'missing':
        return all_percent_series.iloc[all_percent_series.to_numpy().nonzero()]

def distributionValue(df):
    df_temp = df.copy()
    df_temp.dropna(inplace=True)
    a_dict = {}
    a_dict['mean'] = df_temp.mean()
    a_dict['median'] = df_temp.median()
    a_dict['std'] = df_temp.std()
    a_dict['skewness'] = df_temp.skew()
    a_dict['kurtosis'] = kurtosis(df_temp, fisher=False)

    return a_dict

def plotpdf(df, x, kde=True):
    df_temp = df.copy()
    def annotate(data, **kws):
        value = distributionValue(data[x])
        annotate_value = 'mean: {:0.2f}\nstd: {:0.2f}\nskew: {:0.2f}\nkurt: {:0.2f}'.format(value['mean'],value['std'],value['skewness'],value['kurtosis'])
        ax = plt.gca()
        if value['skewness'] < 0:
            x_anotate = 0.05
        else:
            x_anotate = 0.7
        ax.text(x_anotate, .6, annotate_value, transform=ax.transAxes)

    ax = sns.displot(df_temp, x=x, kde=kde)
    ax.map_dataframe(annotate)
    return ax

def plotPoisson(df, x, mu, loc=0):
    df_temp = df.copy()
    x_pmf = x + '_pmf'
    df_temp[x_pmf] = poisson.pmf(df_temp[x], mu=mu, loc=loc)
    df_temp = df_temp[[x, x_pmf]]
    plt.scatter(x=df_temp[x],y=df_temp[x_pmf])
    plt.title('Poisson distribution for {}'.format(x))
    return df_temp

def plotLogNorm(df, x, s, loc, scale):
    df_temp = df.copy()
    x_pdf = x + '_pdf'
    x_log = x + '_log'
    df_temp[x_pdf] = lognorm.pdf(df_temp[x], s, loc, scale)
    df_temp[x_log] = np.log(df_temp[x])
    df_temp2 = df_temp[[x, x_pdf, x_log]]
    df_temp2 = df_temp2.sort_values(x)
    plt.plot(df_temp2[x], df_temp2[x_pdf])
    plt.title('LogNormal distribution for {}'.format(x))
    return df_temp2

def plotWeibull(df, x, c, loc, scale):
    df_temp = df.copy()
    x_pdf = x + '_pdf'
    x_log = x + '_log'
    df_temp[x_pdf] = weibull_min.pdf(df_temp[x], c, loc, scale)
    df_temp2 = df_temp[[x, x_pdf]]
    df_temp2 = df_temp2.sort_values(x)
    plt.plot(df_temp2[x], df_temp2[x_pdf])
    plt.title('Weibull distribution for {}'.format(x))
    return df_temp2

def plotNorm(df, x, loc, scale):
    df_temp = df.copy()
    x_pdf = x + '_pdf'
    x_log = x + '_log'
    df_temp[x_pdf] = norm.pdf(df_temp[x], loc=loc, scale=scale)
    df_temp2 = df_temp[[x, x_pdf]]
    df_temp2 = df_temp2.sort_values(x)
    plt.plot(df_temp2[x], df_temp2[x_pdf])
    plt.title('Guass distribution for {}'.format(x))
    return df_temp2

def deleteColumns(df, columns):
    df_temp = df.copy()
    df_temp.drop(columns, inplace=True, axis=1)
    return df_temp

def deleteRows(df):
    df_temp = df.copy()
    df_temp.dropna(how='any',axis=0, inplace=True)
    return df_temp
