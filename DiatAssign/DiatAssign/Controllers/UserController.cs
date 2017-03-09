using System;
using System.Collections.Generic;
using System.Web.Mvc;
using AutoMapper;
using DiatAssign.BusinessServices;
using DiatAssign.Common.DTOs;
using DiatAssign.Models;

namespace DiatAssign.Controllers
{
    //[ErrorHandle]
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
            var allUsers = Mapper.Map<IEnumerable<UserDto>, IEnumerable<UserVm>>(this._dataService.GetAllUsers());
            return View(allUsers);
        }

        public ActionResult Create()
        {
            return View();
        }

        [HttpPost]
        public ActionResult Create(NewUserVm newUser)
        {
            this._dataService.CreateNewUser(Mapper.Map<NewUserVm, NewUserDto>(newUser));
            return RedirectToAction("Index", "User");
        }

        public ActionResult Edit(int id)
        {
            var toBeUpdated = Mapper.Map<UserDto, UserVm>(this._dataService.GetUserById(id));
            return View(toBeUpdated);
        }

        [HttpPost]
        public ActionResult Edit(UserVm newUser)
        {
            this._dataService.UpdateUser(newUser.Id, Mapper.Map<UserVm, UserDto>(newUser));
            return RedirectToAction("Index", "User");   
        }

        public ActionResult Details(int id)
        {
            var userInfo = Mapper.Map<UserDto, UserVm>(this._dataService.GetUserById(id));
            return View(userInfo); 
        }

        public ActionResult Delete(int id)
        {
            this._dataService.DeleteUser(id);
            return RedirectToAction("Index", "User");
        }
    }
}