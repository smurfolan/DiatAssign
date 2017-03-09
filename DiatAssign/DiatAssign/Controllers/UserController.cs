using System.Collections.Generic;
using System.Web.Mvc;
using DiatAssign.BusinessServices;
using DiatAssign.Models;

namespace DiatAssign.Controllers
{
    public class UserController : Controller
    {
        //private IDataService _dataService;

        //public UserController(IDataService dataService)
        //{
        //    _dataService = dataService;
        //}

        // GET: User
        public ActionResult Index()
        {
            var result = new List<UserVm>()
            {
                new UserVm()
                {
                    Age = 3, FirstName = "Sedsa", LastName = "dsadas", Id = 1
                },
                new UserVm()
                {
                    Age = 6, FirstName = "Weasda", LastName = "dsadas", Id = 2
                }
            };

            return View(result);
        }

        public ActionResult Create()
        {

            return View();
        }

        public ActionResult Edit(int id)
        {
            throw new System.NotImplementedException();
        }

        public ActionResult Details(int id)
        {
            throw new System.NotImplementedException();
        }

        public ActionResult Delete(int id)
        {
            throw new System.NotImplementedException();
        }
    }
}