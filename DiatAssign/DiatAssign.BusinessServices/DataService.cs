using System;
using System.Collections.Generic;
using DiatAssign.Common.DTOs;

namespace DiatAssign.BusinessServices
{
    public class DataService : IDataService
    {
        public IEnumerable<UserDto> GetAllUsers()
        {
            return new List<UserDto>()
            {
                new UserDto()
                {
                    Age = 4,
                    FirstName = "Stef",
                    LastName = "Chov",
                    Id = 4
                },
                new UserDto()
                {
                    Age = 1,
                    FirstName = "somene",
                    LastName = "elseee",
                    Id = 78
                }
            };
        }

        public void CreateNewUser(NewUserDto newUser)
        {
            throw new NotImplementedException();
        }

        public UserDto GetUserById(int userId)
        {
            throw new NotImplementedException();
        }

        public void UpdateUser(int userId, UserDto updatedUser)
        {
            throw new NotImplementedException();
        }

        public void DeleteUser(int userId)
        {
            throw new NotImplementedException();
        }
    }
}
