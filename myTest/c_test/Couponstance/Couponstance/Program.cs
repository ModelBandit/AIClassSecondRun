using System;
using OpenQA.Selenium;
using OpenQA.Selenium.Chrome;
using OpenQA.Selenium.Support.UI;

class Program
{
    //크롬 드라이버 서비스
    static ChromeDriverService m_DriverService;
    //크롬 옵션
    static ChromeOptions m_ChromeOptions;

    //크롬 드라이버 (서비스, 옵션)
    static ChromeDriver m_ChromeDriver;
    static void Main()
    {
        Initialize();
        WorkInPath();
    }

    private static void Initialize()
    {
        m_DriverService = ChromeDriverService.CreateDefaultService();
        m_DriverService.HideCommandPromptWindow = true; // HCPW

        m_ChromeOptions = new ChromeOptions();
        m_ChromeOptions.AddArgument("disable-gpu");

        m_ChromeDriver = new ChromeDriver(m_DriverService, m_ChromeOptions);
    }

    private static void WorkInPath()
    {
        m_ChromeDriver.Navigate().GoToUrl("https://coupon.a.prod.service.trickcal.io/");
        m_ChromeDriver.Manage().Timeouts().ImplicitWait = TimeSpan.FromSeconds(10);

        //f12로 개발자 화면을 열어서 해당 구간에 해당하는 곳에서 마우스 오른쪽 클릭의 copy에서 얻은 xpath를 사용함
        string UIDXPath = "//*[@id='UserId']";
        IWebElement UIDBox = m_ChromeDriver.FindElement(By.XPath(UIDXPath));
        UIDBox.SendKeys("");

        string CouponPath = "//*[@id='CouponCode']";
        IWebElement CouponBox = m_ChromeDriver.FindElement(By.XPath(CouponPath));
        CouponBox.SendKeys("");

        string ButtonPath = "//*[@id=\"couponForm\"]/div[2]/button";
        IWebElement Button = m_ChromeDriver.FindElement(By.XPath(ButtonPath));
        Button.Click();
    }
}