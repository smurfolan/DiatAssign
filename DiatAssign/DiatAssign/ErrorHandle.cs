using System.Web.Mvc;

namespace DiatAssign
{
    public class ErrorHandle : HandleErrorAttribute
    {
        public override void OnException(ExceptionContext filterContext)
        {
            // TODO: Log exception
            var ex = filterContext.Exception;
            filterContext.ExceptionHandled = true;

            filterContext.Result = new ViewResult()
            {
                ViewName = "Error",
            };
        }
    }
}