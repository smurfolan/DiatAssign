using DiatAssign.DataModel.Entities;

namespace DiatAssign.DataModel.Migrations
{
    using System.Data.Entity.Migrations;

    internal sealed class Configuration : DbMigrationsConfiguration<DataContext>
    {
        public Configuration()
        {
            AutomaticMigrationsEnabled = false;
        }

        protected override void Seed(DiatAssign.DataModel.DataContext context)
        {
            //  This method will be called after migrating to the latest version.

            //  You can use the DbSet<T>.AddOrUpdate() helper extension method 
            //  to avoid creating duplicate seed data. E.g.

            context.Users.AddOrUpdate(
              u => u.Id,
              new User() { Id = 1, Age = 35, FirstName = "Stephen", LastName = "Jefferson"},
              new User() { Id = 2, Age = 21, FirstName = "Page", LastName = "Heaton" },
              new User() { Id = 3, FirstName = "Alfred", LastName = "Manson" }
            );

        }
    }
}
