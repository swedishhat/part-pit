uses IOUtils;

procedure TForm2.Button1Click(Sender: TObject);
var
  LList: TStringDynArray;
  I: Integer;
  LSearchOption: TSearchOption;
begin
  { Select the search option }
  if cbDoRecursive.Checked then
    LSearchOption := TSearchOption.soAllDirectories
  else
    LSearchOption := TSearchOption.soTopDirectoryOnly;

  try
    { For all entries use GetFileSystemEntries method }
    if cbIncludeDirectories.Checked and cbIncludeFiles.Checked then
      LList := TDirectory.GetFileSystemEntries(edtPath.Text, LSearchOption, nil);

    { For directories use GetDirectories method }
    if cbIncludeDirectories.Checked and not cbIncludeFiles.Checked then
      LList := TDirectory.GetDirectories(edtPath.Text, edtFileMask.Text, LSearchOption);

    { For files use GetFiles method }
    if not cbIncludeDirectories.Checked and cbIncludeFiles.Checked then
      LList := TDirectory.GetFiles(edtPath.Text, edtFileMask.Text, LSearchOption);
  except
    { Catch the possible exceptions }
    MessageDlg('Incorrect path or search mask', mtError, [mbOK], 0);
    Exit;
  end;

  { Populate the memo with the results }
  mmResults.Clear;

  for I := 0 to Length(LList) - 1 do
    mmResults.Lines.Add(LList[I]);
end;

