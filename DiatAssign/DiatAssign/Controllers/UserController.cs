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
        private readonly IDataService _dataService;

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
            catch (Exception ex)
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

                return RedirectToAction("Index", "User");
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
            try
            {
                var userInfo = Mapper.Map<UserDto, UserVm>(this._dataService.GetUserById(id));

                return View(userInfo);
            }
            catch (Exception)
            {
                // TODO: Log error
                return View("Error");
            }

            
        }

        public ActionResult Delete(int id)
        {
            try
            {
                this._dataService.DeleteUser(id);
                return RedirectToAction("Index", "User");
            }
            catch (Exception)
            {
                // TODO: Log error
                return View("Error");
            }
        }
    }
}