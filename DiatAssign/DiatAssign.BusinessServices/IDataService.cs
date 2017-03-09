using System.Collections.Generic;
using DiatAssign.Common.DTOs;

namespace DiatAssign.BusinessServices
{
    public interface IDataService
    {
        IEnumerable<UserDto> GetAllUsers();
        void CreateNewUser(NewUserDto newUser);
        UserDto GetUserById(int userId);
        void UpdateUser(int userId, UserDto updatedUser);
        void DeleteUser(int userId);
    }
}
