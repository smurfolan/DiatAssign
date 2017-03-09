using System.Reflection;
using System.Web.Mvc;
using System.Web.Optimization;
using System.Web.Routing;
using DiatAssign.BusinessServices;
using Ninject;
using Ninject.Web.Common;

namespace DiatAssign
{
    public class MvcApplication : NinjectHttpApplication
    {
        protected override void OnApplicationStarted()
        {
            AreaRegistration.RegisterAllAreas();
            FilterConfig.RegisterGlobalFilters(GlobalFilters.Filters);
            RouteConfig.RegisterRoutes(RouteTable.Routes);
            BundleConfig.RegisterBundles(BundleTable.Bundles);

            AutoMapperConfiguration.Configure();
        }

        protected override IKernel CreateKernel()
        {
            var kernel = new StandardKernel();

            kernel.Load(Assembly.GetExecutingAssembly());

            kernel.Bind<IDataService>().To<DataService>();

            return kernel;
        }
    }
}
