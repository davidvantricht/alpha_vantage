from .alphavantage import AlphaVantage as av

from datetime import datetime
search_date = datetime.now().date().strftime('%Y-%m-%d')

class FundamentalData(av):

    """This class implements all the api calls to fundamental data
    """
    def __init__(self, *args, **kwargs):
        """
        Inherit AlphaVantage base class with its default arguments.
        """
        super(FundamentalData, self).__init__(*args, **kwargs)
        self._append_type = False
        if self.output_format.lower() == 'csv':
            raise ValueError("Output format {} is not compatible with the FundamentalData class".format(
                self.output_format.lower()))

    @av._output_format
    @av._call_api_on_func
    def get_company_overview(self, symbol):
        """
        Returns the company information, financial ratios, 
        and other key metrics for the equity specified. 
        Data is generally refreshed on the same day a company reports its latest 
        earnings and financials.

        Keyword Arguments:
            symbol:  the symbol for the equity we want to get its data
        """
        _FUNCTION_KEY = 'OVERVIEW'
        return _FUNCTION_KEY, None, None
    
    @av._output_format
    @av._call_api_on_func
    def get_income_statement_annual(self, symbol):
        """
        Returns the annual and quarterly income statements for the company of interest. 
        Data is generally refreshed on the same day a company reports its latest 
        earnings and financials.

        Keyword Arguments:
            symbol:  the symbol for the equity we want to get its data
        """
        _FUNCTION_KEY = 'INCOME_STATEMENT'
        return _FUNCTION_KEY, 'annualReports', 'symbol'

    @av._output_format
    @av._call_api_on_func
    def get_income_statement_quarterly(self, symbol):
        """
        Returns the annual and quarterly income statements for the company of interest. 
        Data is generally refreshed on the same day a company reports its latest 
        earnings and financials.

        Keyword Arguments:
            symbol:  the symbol for the equity we want to get its data
        """
        _FUNCTION_KEY = 'INCOME_STATEMENT'
        return _FUNCTION_KEY, 'quarterlyReports', 'symbol'

    @av._output_format
    @av._call_api_on_func
    def get_balance_sheet_annual(self, symbol):
        """
        Returns the annual and quarterly balance sheets for the company of interest.
        Data is generally refreshed on the same day a company reports its latest 
        earnings and financials.

        Keyword Arguments:
            symbol:  the symbol for the equity we want to get its data
        """
        _FUNCTION_KEY = 'BALANCE_SHEET'
        return _FUNCTION_KEY, 'annualReports', 'symbol'

    @av._output_format
    @av._call_api_on_func
    def get_balance_sheet_quarterly(self, symbol):
        """
        Returns the annual and quarterly balance sheets for the company of interest.
        Data is generally refreshed on the same day a company reports its latest 
        earnings and financials.

        Keyword Arguments:
            symbol:  the symbol for the equity we want to get its data
        """
        _FUNCTION_KEY = 'BALANCE_SHEET'
        return _FUNCTION_KEY, 'quarterlyReports', 'symbol'

    @av._output_format
    @av._call_api_on_func
    def get_cash_flow_annual(self, symbol):
        """
        Returns the annual and quarterly cash flows for the company of interest.
        Data is generally refreshed on the same day a company reports its latest 
        earnings and financials.

        Keyword Arguments:
            symbol:  the symbol for the equity we want to get its data
        """
        _FUNCTION_KEY = 'CASH_FLOW'
        return _FUNCTION_KEY, 'annualReports', 'symbol'

    @av._output_format
    @av._call_api_on_func
    def get_cash_flow_quarterly(self, symbol):
        """
        Returns the annual and quarterly cash flows for the company of interest.
        Data is generally refreshed on the same day a company reports its latest 
        earnings and financials.

        Keyword Arguments:
            symbol:  the symbol for the equity we want to get its data
        """
        _FUNCTION_KEY = 'CASH_FLOW'
        return _FUNCTION_KEY, 'quarterlyReports', 'symbol'

    @av._output_format
    @av._call_api_on_func
    def get_listing_status(self):
        """
        Returns a list of active or delisted US stocks and ETFs, either as of the
        latest trading day or at a specific time in history. The endpoint is
        positioned to facilitate equity research on asset lifecycle and survivorship.
        Keyword Arguments:
            date:   If no date is set, the API endpoint will return a list of active
                    or delisted symbols as of the latest trading day. If a date is set,
                    the API endpoint will "travel back" in time and return a list of
                    active or delisted symbols on that particular date in history.
                    Any YYYY-MM-DD date later than 2010-01-01 is supported.
                    For example, date=2013-08-03
            state:  By default, state=active and the API will return a list of actively
                    traded stocks and ETFs. Set state=delisted to query a list of
                    delisted assets.
        """
        _FUNCTION_KEY = 'LISTING_STATUS'
        return _FUNCTION_KEY, 'date', 'state'