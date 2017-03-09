using AutoMapper;
using DiatAssign.Common.DTOs;
using DiatAssign.Models;

namespace DiatAssign
{
    public static class AutoMapperConfiguration
    {
        public static void Configure()
        {
            Mapper.Initialize(cfg =>
            {
                cfg.AddProfile(new UserProfile());
            });
        }
    }

    public class UserProfile : Profile
    {
        public UserProfile()
        {
            CreateMap<UserDto, UserVm>();
            CreateMap<NewUserVm, NewUserDto>();
        }
    }
}