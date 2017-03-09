using System.Data.Entity;
using DiatAssign.DataModel.Entities;

namespace DiatAssign.DataModel
{
    public class DataContext : DbContext
    {
        public IDbSet<User> Users { get; set; }
    }
}
