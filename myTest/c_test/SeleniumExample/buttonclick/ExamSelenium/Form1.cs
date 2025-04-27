using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading;
using System.Threading.Tasks;
using System.Windows.Forms;
using System.Diagnostics;
using OpenQA.Selenium;
using OpenQA.Selenium.Chrome;
using OpenQA.Selenium.Support.UI;

namespace ExamSelenium
{
    public partial class Form1 : Form
    {
        protected ChromeDriverService _driverService = null;
        protected ChromeOptions _options = null;
        protected ChromeDriver _driver = null;

        public Form1()
        {
            InitializeComponent();

            try
            {
                _driverService = ChromeDriverService.CreateDefaultService();
                _driverService.HideCommandPromptWindow = true;

                _options = new ChromeOptions();
                _options.AddArgument("disable-gpu");
            }
            catch(Exception exc)
            {
                Trace.WriteLine(exc.Message);
            }
        }

        private void buttonLogin_Click(object sender, EventArgs e)
        {
            try
            {
                _driver = new ChromeDriver(_driverService, _options);

                _driver.Navigate().GoToUrl("https://www.naver.com");

                _driver.Manage().Timeouts().ImplicitWait = TimeSpan.FromSeconds(10);

                var searchBox = _driver.FindElementByXPath("//*[@id='query']");
                searchBox.SendKeys(textBox1.Text);

                var searchButton = _driver.FindElementByXPath("//*[@id='search_btn']");
                searchButton.Click();
            }
            catch (Exception exc)
            {
                Trace.WriteLine(exc.Message);
            }
        }

        private void Form1_FormClosing(object sender, FormClosingEventArgs e)
        {
            _driver.Quit();
        }
    }
}
