using System.Collections.Generic;
using System.Linq;
using DiatAssign.Common.DTOs;
using DiatAssign.DataModel;
using DiatAssign.DataModel.Entities;

namespace DiatAssign.BusinessServices
{
    public class DataService : IDataService
    {
        // What I usually do in this case, up here I use Repository or Unit of Work. This case is not so complex so I decided to skip it.

        public IEnumerable<UserDto> GetAllUsers()
        {
            using (var dbContext = new DataContext())
            {
                return
                    dbContext.Users.Select(
                        u => new UserDto() {Age = u.Age, Id = u.Id, FirstName = u.FirstName, LastName = u.LastName})
                        .ToList();
            }
        }

        public void CreateNewUser(NewUserDto newUser)
        {
            using (var dbContext = new DataContext())
            {
                var newEntity = new User()
                {
                    Age = newUser.Age, FirstName = newUser.FirstName, LastName = newUser.LastName
                };

                dbContext.Users.Add(newEntity);

                dbContext.SaveChanges();
            }
        }

        public UserDto GetUserById(int userId)
        {
            using (var dbContext = new DataContext())
            {
                var result = dbContext.Users.FirstOrDefault(u => u.Id == userId);

                if (result == null)
                    return null;

                return new UserDto()
                {
                    Age = result.Age,
                    FirstName = result.FirstName,
                    LastName = result.LastName,
                    Id = result.Id
                };
            }
        }

        public void UpdateUser(int userId, UserDto updatedUser)
        {
            using (var dbContext = new DataContext())
            {
                var toBeUpdated = dbContext.Users.FirstOrDefault(u => u.Id == userId);
                if (toBeUpdated == null)
                    return;

                toBeUpdated.Age = updatedUser.Age;
                toBeUpdated.FirstName = updatedUser.FirstName;
                toBeUpdated.LastName = updatedUser.LastName;

                dbContext.SaveChanges();
            }
        }

        public void DeleteUser(int userId)
        {
            using (var dbContext = new DataContext())
            {
                var toBeDeleted = dbContext.Users.FirstOrDefault(u => u.Id == userId);
                dbContext.Users.Remove(toBeDeleted);

                dbContext.SaveChanges();
            }
        }
    }
}
