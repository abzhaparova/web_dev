import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';
import { VacanciesComponent } from './vacancies/vacancies.component';
import { MainComponent } from './main/main.component';


const routes: Routes = [
  {path: '', component: MainComponent},
  //{path: '', redirectTo:'/companies', pathMatch:'full'},
  {path:'companies/:id/vacancies', component:VacanciesComponent}
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
