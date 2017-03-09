using System;
using System.Collections.Generic;
using System.Web.Mvc;
using AutoMapper;
using DiatAssign.BusinessServices;
using DiatAssign.Common.DTOs;
using DiatAssign.Models;

namespace DiatAssign.Controllers
{
    public class UserController : Controller
    {
        private IDataService _dataService;

        public UserController(IDataService dataService)
        {
            _dataService = dataService;
        }

        // GET: User
        public ActionResult Index()
        {
            try
            {
                var allUsers = Mapper.Map<IEnumerable<UserDto>, IEnumerable<UserVm>>(this._dataService.GetAllUsers());

                return View(allUsers);
            }
            catch (Exception)
            {
                // TODO: Log error
                return View("Error");
            }
        }

        public ActionResult Create()
        {
            return View();
        }

        [HttpPost]
        public ActionResult Create(NewUserVm newUser)
        {
            try
            {
                this._dataService.CreateNewUser(Mapper.Map<NewUserVm, NewUserDto>(newUser));

                return View("Index");
            }
            catch (Exception)
            {
                // TODO: Log error
                return View("Error");
            }
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